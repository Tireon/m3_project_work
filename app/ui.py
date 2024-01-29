from objectpack.ui import BaseEditWindow
from m3_ext.ui import all_components as ext

class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label='password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label='last_login',
            name='last_login',
            allow_blank=False,
            anchor='100%',
            format='d.m.Y')

        self.field__superuser_status = ext.ExtCheckBox(
            label='superuser_status',
            name='superuser_status',
            allow_blank=False,
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label='username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label='first_name',
            name='first_name',
            allow_blank=False,
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label='last_name',
            name='last_name',
            allow_blank=False,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label='email',
            name='email',
            allow_blank=False,
            anchor='100%')

        self.field__staff_status = ext.ExtCheckBox(
            label='staff_status',
            name='staff_status',
            allow_blank=False,
            anchor='100%')

        self.field__active = ext.ExtCheckBox(
            label='active',
            name='active',
            allow_blank=False,
            anchor='100%')

        self.field__date_joined = ext.ExtDateField(
            label='date_joined',
            name='date_joined',
            allow_blank=False,
            anchor='100%',
            format='d.m.Y')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__superuser_status,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__staff_status,
            self.field__active,
            self.field__date_joined,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'
