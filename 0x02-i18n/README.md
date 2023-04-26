# 0x02. i18n
`Flask-Babel`

## Learning objectives
- Parametrize flask templates to display different languages
- Infer the correct locale based on URL parameters, user settings or request headers
- Localize timestamps

## Tasks
### 0.Basic Flask app

Setup a basic flask app and create a single route `/` and a template that outputs `Hello World`

### 1.Basic Babel setup

Install the Babel Flask extension
```
pip install flask_babel
```
Instantiate the Babel object in your app. Store it in a module-level variable named babel.

In order to configure available languages in your app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale ("en") and timezone ("UTC").Use that class as config for your Flask app.

### 2.Get locale from request

Create a `get_locale` function with the `babel.localeselector decorator`. Use `request.accept_languages` to determine the best match with our supported languages.

### 3.Parametrize templates

Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

Create a babel.cfg file containing:
```
[python: **.py]
[jinja2: **/templates/**.html]
```
Initialize your translations with:
```
pybabel extract -F babel.cfg -o messages.pot .
```
and your two dictionaries with:
```
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l fr
```
Then edit files with the `.po` extension (`translations/[en|fr]/LC_MESSAGES/messages.po`) to provide the correct value for each message ID for each language. Use the following translations: