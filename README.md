![license](https://img.shields.io/github/license/Radonirinaunimi/python-template?style=flat-square)
![repo size](https://img.shields.io/github/repo-size/Radonirinaunimi/python-template?style=flat-square)
### Python template

**Python-template** serves as a general template to start a python project. It's aim is to automatize the development workflow: from packaging the code, generating documentation, deploying and releasing the package. So far, the development workflow is based on the following steps:
* The *packaging* of the distributions is taken care by the [Distribution Utilities](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/introduction.html) (Disutils) throught the `setup.py` file. This allows users (or developers) to easily install (or to simulate the installation by adding a symbolic link for easy debug) the package into a particular environment.
* For stability, the modules of the *packaged-library* can be automatically tested using `pytest`. This helps prevent breaking the code when new features are added. The coverage of the tests can then be assessed afterward; the more modules undergo testing the less likely a bug is present. Refer to the web [documentation](https://docs.pytest.org/en/stable/) for further details on how to use pytest for testing.
* The documentation of the modules can be automatically generated from the [doc](https://github.com/Radonirinaunimi/python-template/tree/master/doc) folder. This generates documentation of [this style](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/introduction.html) using **sphinx**. To familiarize with sphinx, have a look at the following [documentation](https://www.sphinx-doc.org/en/master/usage/quickstart.html).
* Finally, all of the above can be integrated within **github** using the [github actions](https://docs.pytest.org/en/stable/) [CI/CD](https://github.blog/2019-08-08-github-actions-now-supports-ci-cd/). This allows one to test the package at every push (for instance) and ti deploy the documentation. The follwoing [documentation](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions) explains the syntax for writting a github action.


#### How to use this template

In order to use this template, first, one has to replace `<package_name>` in the following files [setup.py](https://github.com/Radonirinaunimi/python-template/blob/master/setup.py#L16), [Makefile](https://github.com/Radonirinaunimi/python-template/blob/master/doc/Makefile#L12), [conf.py](https://github.com/Radonirinaunimi/python-template/blob/master/doc/source/conf.py#L14) by the **name** of the package. Then, add the requierement the package is depending to [here](https://github.com/Radonirinaunimi/python-template/blob/master/setup.py#L23). Essentially, these the only things one need to package the distribution. In oder to install the package, run the following on the terminal:
```bash
python setup.py install --user
```
or if you are a developer
```bash
python setup.py develop --user
```
To generate the documentation, go inside the [doc](https://github.com/Radonirinaunimi/python-template/tree/master/doc) folder and run the following command:
```bash
make html
```
Before pushing to the github, ...
Explanation about generating tokes, ...
