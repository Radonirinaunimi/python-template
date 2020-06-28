# Makefile for Sphinx documentation

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Custom directory
# Replace <package_name> by the name of the package
PACKAGEDIR = ../src/<package_name>
PACKAGETESTDIR = ../src/<package_name>/tests

# If there is no argument provided to make, then print out help
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile clean

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	sphinx-apidoc -o ./source/modules/pycompressor "$(PACKAGEDIR)" "$(PACKAGETESTDIR)"
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

view: html
	$(BROWSER) $(BUILDDIR)/html/index.html

clean:
	rm -rf build
