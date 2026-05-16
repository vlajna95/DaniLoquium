@echo off
pybabel extract --mapping babel.cfg --no-wrap --msgid-bugs-address="dani@danimundo.com" --copyright-holder="Danijela Popovic" --project="DaniLoquium" --version="1.0" --add-comments=Translators:,TRANSLATORS: --strip-comments --output themes\localized_Elegance\translations\%2.pot .
if "%~1"=="init" (
	pybabel init --locale %3 --input-file themes\localized_Elegance\translations\%2.pot --output-dir themes\localized_Elegance\translations --domain %2
) else if "%~1"=="update" (
	pybabel update --input-file themes\localized_Elegance\translations\%2.pot --no-wrap --update-header-comment --output-dir themes\localized_Elegance\translations --domain %2
) else (
	echo "The action must be specified."
)
