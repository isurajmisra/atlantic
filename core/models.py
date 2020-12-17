import os
import secrets
import sys
import uuid
from io import BytesIO
from magic import Magic
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django_resized import ResizedImageField
# Create your models here.


class Slideshow(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="img/banner/")
    link = models.URLField(null=True, blank=True)

class Gallery(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="img/gallery/")

class LogoFav(models.Model):
    logo = models.ImageField(null=True, blank=True, upload_to="img/logo/")
    fav = models.ImageField(null=True, blank=True, upload_to="img/fav/")

class ServiceSubCategory(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="img/subcategory/")
    title = models.CharField(max_length=50,null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)

class ServiceCategory(models.Model):
    title = models.CharField(max_length=50,null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    subcategory = models.ManyToManyField(ServiceSubCategory, null=True, blank=True)
    
class ModifiedImg(models.Model):
    banner = models.ForeignKey(Slideshow, null=True, blank=True, on_delete=models.CASCADE)
    banner_desktop = models.ImageField(null=True, blank=True, upload_to="img/modifiedImg/desktop/")
    banner_tablet = models.ImageField(null=True, blank=True, upload_to="img/modifiedImg/tablet/")
    banner_mobile = models.ImageField(null=True, blank=True, upload_to="img/modifiedImg/mobile/")

    def save(self, *args, **kwargs):

        if not self.id and not self.banner_desktop and not self.banner_tablet and not self.banner_mobile:
            return

        super(ModifiedImg, self).save(*args, **kwargs)

        desk_image = Image.open(self.banner_desktop)
        desk_image = desk_image.resize((2000, 500))
        desk_image.save(self.banner_desktop.path)
        desk_image.close()

        tab_image = Image.open(self.banner_tablet)
        tab_image = tab_image.resize((800, 500))
        tab_image.save(self.banner_tablet.path)
        tab_image.close()

        mob_image = Image.open(self.banner_mobile)
        mob_image = mob_image.resize((600, 500))
        mob_image.save(self.banner_mobile.path)
        mob_image.close()



VALID_IMAGE_MIMETYPES = [
    "image"
]
VALID_IMAGE_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
]




def get_mimetype(fobject):
    mime = Magic(mime=True)
    mimetype = mime.from_buffer(fobject.read(1024))
    fobject.seek(0)
    return mimetype

def valid_image_mimetype(fobject):
    mimetype = get_mimetype(fobject)
    if mimetype:
        return mimetype.startswith('image')
    else:
        return False

def validate_image(image):
    file_size = image.size
    limit_mb = 5
    # valid = valid_image_mimetype(image)
    base = os.path.basename(image.name)
    filename= os.path.splitext(base)[0]
    ext = os.path.splitext(base)[1]
    # if file_size > limit_mb * 1024*1024*5:
    #     msg = "Max size of file is %s MB" % limit_mb
    #     return False, msg, image
    # elif not valid:
    #     msg = "Image mimetype is invalid"
    #     return False, msg, image
    if ext not in VALID_IMAGE_EXTENSIONS:
        msg = "Invalid File extension."
        return False, msg, image
    # random_hex = secrets.token_hex(4)
    image.name = base
    return image


@receiver(post_save, sender=Slideshow)
def signal_deposit_save(sender, instance, created, **kwargs):
    if created:
        img = instance.img.file
        im_desktop = validate_image(img)
        im_tablet = validate_image(img)
        im_mobile = validate_image(img)

        modified_imgs = ModifiedImg.objects.create(banner=instance)
        modified_imgs.banner_desktop = im_desktop
        modified_imgs.banner_tablet = im_tablet
        modified_imgs.banner_mobile = im_mobile

        modified_imgs.save()

