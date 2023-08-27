# Описание

# django-editor-ymaps
если у вас Django >=4.0.0, то что бы заработал 'djeym' нужно заменить 
1) ugettext на gettext
2) ugettext_lazy на gettext_lazy
3) ungettext_lazy на ngettext_lazy
3) force_text на force_str

при ошибки захода на исправление маркеров в админке 
1. Убедитесь, что у вас установлен и настроен пакет CKEditor. Установите CKEditor с помощью pip:
pip install django-ckeditor
2. В файле settings.py вашего Django проекта, добавьте 'ckeditor' в список установленных приложений:

INSTALLED_APPS = [
    ...
    'ckeditor',
    ...
]
3. Убедитесь, что вы настроили CKEditor в вашем проекте. В файле settings.py добавьте следующие строки:

\# django-ckeditor
\# https://github.com/django-ckeditor/django-ckeditor
CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_FILENAME_GENERATOR = 'djeym.utils.get_filename'
CKEDITOR_THUMBNAIL_SIZE = (300, 300)
CKEDITOR_FORCE_JPEG_COMPRESSION = True
CKEDITOR_IMAGE_QUALITY = 40
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_ALLOW_NONIMAGE_FILES = False  # False - Only image files. (At your discretion)
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 400,
        'width': '100%',
    },
    'djeym': {
        'toolbar': 'full',
        'height': 400,
        'width': 362,
        'colorButton_colors': 'F44336,C62828,E91E63,AD1457,9C27B0,6A1B9A,'
                              '673AB7,4527A0,3F51B5,283593,2196F3,1565C0,'
                              '03A9F4,0277BD,00BCD4,00838F,009688,00695C,'
                              '4CAF50,2E7D32,8BC34A,558B2F,CDDC39,9E9D24,'
                              'FFEB3B,F9A825,FFC107,FF8F00,FF9800,EF6C00,'
                              'FF5722,D84315,795548,4E342E,607D8B,37474F,'
                              '9E9E9E,424242,000000,FFFFFF',
        'colorButton_enableAutomatic': False,
        'colorButton_enableMore': True
    }
}

4. Выполните миграции, чтобы применить изменения:

python manage.py migrate

5. Если у вас есть кеш Django, попробуйте очистить его. В консоли выполните следующую команду:

python manage.py clearcache

После выполнения этих действий, перезапустите ваш сервер Django и попробуйте снова добавить маркер. Ошибка "TemplateDoesNotExist: ckeditor/widget.html" должна быть исправлена

Если после выполнения 

py manage.py makemigrations djeym

получаете ошибку
PermissionError: [Errno 13] Permission denied: 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python39_64\\lib\\site-packages\\djeym\\migrations\\0002_alter_blockedip_id_alter_categoryplacemark_id_and_more.py'

выполните команду в консоли с правами администратора
