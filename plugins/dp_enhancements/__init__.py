import os
import shutil
# import subprocess
from pelican import signals
from .dp_export_articles import export_articles
from .dp_underline_extension import makeExtension as underline_makeExtension
from .dp_speaktext_extension import makeExtension as speaktext_makeExtension


def add_underline_extension(pelicanobj):
	pelicanobj.settings["MARKDOWN"].setdefault("extensions", []).append(underline_makeExtension())


def add_speaktext_extension(pelicanobj):
	pelicanobj.settings["MARKDOWN"].setdefault("extensions", []).append(speaktext_makeExtension())


def test_context(instance, metadata):
	metadata["exports"] = list(instance.settings.get("EXPORT_OPTIONS").keys())


def copy_output_files(pelican_obj):
	print("Copying output files to the www...")
	# subprocess.run("cp -r /home/dev/DaniLoquium/output_fr/* /var/www/DaniLoquium-fr/", shell=True)
	source_dir = "/home/dev/DaniLoquium/output_fr"
	destination_dir = "/var/www/DaniLoquium-fr"
	if not os.path.exists(destination_dir):
		os.makedirs(destination_dir)
	for item in os.listdir(source_dir):
		s = os.path.join(source_dir, item)
		d = os.path.join(destination_dir, item)
		if os.path.isdir(s):
			if os.path.exists(d):
				shutil.rmtree(d)
			shutil.copytree(s, d)
		else:
			shutil.copy2(s, d)


def register():
	signals.initialized.connect(add_underline_extension)
	signals.initialized.connect(add_speaktext_extension)
	signals.article_generator_context.connect(test_context)
	signals.article_generator_finalized.connect(export_articles)
	# signals.finalized.connect(copy_output_files)
