print(f'hello world');

print(f'***Sistema de Generador de Emails***');

nombre_usuario = 'Laura Martinez Soto';
nombre_usuario_normalizado = nombre_usuario.replace(' ', '.').lower();

print(f'Nombre de usuario: {nombre_usuario} ');
print(f'Nombre de usuario normalizado: {nombre_usuario_normalizado} ');
print(f'\n');

nombre_empresa = 'La Casa de la Cultura';
extension_dominio = '.cultura.com';
dominio_mail = nombre_empresa.replace(' ', '').lower() + extension_dominio;

print(f'nombre empresa: {nombre_empresa} ');
print(f'extension dominio: {extension_dominio} ');
print(f'dominio de email normalizado: {dominio_mail}');
print(f'\n');

email_final_generado = nombre_usuario_normalizado + '@' + dominio_mail;
print(f'Email generado: {email_final_generado} ');