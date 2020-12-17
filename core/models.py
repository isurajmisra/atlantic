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
    img = models.ImageField(null=True, blank=True, upload_to="core/static/img/banner/")
    link = models.URLField(null=True, blank=True)

class Gallery(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="core/static/img/gallery/")

class LogoFav(models.Model):
    logo = models.ImageField(null=True, blank=True, upload_to="core/static/img/logo/")
    fav = models.ImageField(null=True, blank=True, upload_to="core/static/img/fav/")

class ServiceSubCategory(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="core/static/img/subcategory/")
    title = models.CharField(max_length=50,null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)

class ServiceCategory(models.Model):
    title = models.CharField(max_length=50,null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    subcategory = models.ManyToManyField(ServiceSubCategory, null=True, blank=True)
    
class ModifiedImg(models.Model):
    banner = models.ForeignKey(Slideshow, null=True, blank=True, on_delete=models.CASCADE)
    banner_desktop = ResizedImageField(size=[2000, 500] ,null=True, blank=True, upload_to="core/static/img/modifiedImg/desktop/")
    banner_tablet = ResizedImageField(size=[800, 500] ,null=True, blank=True, upload_to="core/static/img/modifiedImg/tablet/")
    banner_mobile = ResizedImageField(size=[600, 500] ,null=True, blank=True, upload_to="core/static/img/modifiedImg/mobile/")

    # def save(self):
    #     # Opening the uploaded image
    #     im = Image.open(self.img)
    #
    #     output = BytesIO()
    #
    #     # Resize/modify the image
    #     im = im.resize((100, 100))
    #
    #     # after modifications, save it to the output
    #     im.save(output, format='JPEG', quality=100)
    #     output.seek(0)
    #
    #     # change the imagefield value to be the newley modifed image value
    #     self.img = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.img.name.split('.')[0], 'image/jpeg',
    #                                     sys.getsizeof(output), None)
    #
    #     super(ModifiedImg, self).save()
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

# def get_file_path(instance, filename, text):
#     ext = filename.split('.')[-1]
#     filename = f"{text}" % (uuid.uuid4(), ext)
#     return os.path.join(instance.directory_string_var, filename)

@receiver(post_save, sender=Slideshow)
def signal_deposit_save(sender, instance, created, **kwargs):
    if created:
        img = instance.img.file
        im_desktop = validate_image(img)
        im_tablet = validate_image(img)
        im_mobile = validate_image(img)
        # # # im_desktop.save("core\static\img\im_desktop.jpg")
        # # # im_tablet.save("core\static\img\im_tablet.jpg")
        # # # im_mobile.save("core\static\img\im_mobile.jpg")
        # im_desktop.filename = get_file_path(instance, img.filename, "_desktop")
        modified_imgs = ModifiedImg.objects.create(banner=instance)
        modified_imgs.banner_desktop = im_desktop
        modified_imgs.banner_tablet = im_tablet
        modified_imgs.banner_mobile = im_mobile

        modified_imgs.save()

