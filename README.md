<table style="width:100%">
  <tr>
    <td rowspan="2" style="width:50px">
      <img alt="Logo" src="https://github.com/Radonirinaunimi/python-template/blob/master/logo/logo.png" width=50%>
    </td>
    <td>
      <img src="https://img.shields.io/badge/python_template-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
      <img src="https://img.shields.io/badge/LICENSE:_MIT-ED1C24?style=for-the-badge"/>
    </td>
  </tr>
  <tr>
    <td> 
      <p align="justify">
        <b>pytemplate</b> serves as a general template to start a python project. It aims to automate the development workflow: from 
        packaging the code, generating documentation, versioning, deploying and releasing the package.
      </p>
    </td>
  </tr>
</table>

## Description

The development workflow is based on the following steps:
<p align="justify">
  <b> Packaging </b> 📦
  The packaging of the distribution is managed by the 
  <a href="https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/introduction.html">Distribution Utilities</a> (Disutils).
  This allows users (or developers) to easily install the package (or to simulate the installation by adding a symbolic link for easy debug) 
  into a particular environment.
</p>

<p align="justify">
  <b> Continuous testing </b> 🛠️
  For stability, the modules of the packaged-library can be automatically tested using <b>pytest</b>. This helps prevent breaking the code 
  when new features are added. These tests can be run as github-actions when the events are triggered (as will be detailed further). The 
  coverage of the tests can then be assessed afterward; the more modules undergo testing the less likely bugs occur. Refer to the web
  <a href="https://docs.pytest.org/en/stable/">documentation</a> for further details on how to use pytest for testing.
</p>

<p align="justify">
  <b> Documentation </b> 📚
  The documentation of nodules is built using the following 
  <a href="https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/introduction.html">style</a> with <b>sphinx</b>. To 
  familiarize with sphinx, have a look at the following <a href="https://www.sphinx-doc.org/en/master/usage/quickstart.html">documentation</a>.
</p>

<p align="justify">
  <b> Documentation </b> 🚀
  Finally, all of the above can be integrated within github using <a href="https://docs.pytest.org/en/stable/">github actions</a>
  <a href="https://github.blog/2019-08-08-github-actions-now-supports-ci-cd/">CI/CD</a>. This allows one to test the package at every 
  push (for instance) and deploys the documentation. The follwoing 
  <a href="https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions">documentation</a> explains the syntax for writting 
  a github action.
</p>


## How to use this template

### Setting up ⚙️

<p align="justify">
  In order to use this template, first, click on <a href="https://github.com/Radonirinaunimi/python-template/generate">use this template</a>. 
  Then, replace all mentions of package_name in the following files <a href="https://github.com/Radonirinaunimi/python-template/blob/master/setup.py#L16">
  setup.py</a>, <a href="https://github.com/Radonirinaunimi/python-template/blob/master/doc/Makefile#L12">Makefile</a>, 
  <a href="https://github.com/Radonirinaunimi/python-template/blob/master/.github/workflows/test_modules.yml">test_modules.yml</a>, 
  <a href="https://github.com/Radonirinaunimi/python-template/blob/master/doc/source/conf.py#L14">conf.py</a> by the <b>name</b> of the package. 
  The next step is to add the requierements the package is depending to 
  <a href="https://github.com/Radonirinaunimi/python-template/blob/master/requirements.txt">requirements.txt</a>. Essentially, these the only things 
  one need to package the distribution. The package is now ready for installation by running the following:  
</p>

```bash
python setup.py install [--user]
```
or alternatively (if you are a developer) by adding symbolic links which immediately reflects the changes after every save:
```bash
python setup.py develop [--user]
```

### Checking, formatting and testing the code

<p align="justify">
  Using static code analysis tools can be extremely helpful in terms of checking programming errors and enforcing coding standards. As an analysis tool,
  this template uses <a href="https://pylint.org/">pylint</a> which is highly customazable. The default configurations are given in the
  <a href="https://github.com/Radonirinaunimi/python-template/blob/master/.pylintrc">.pylintrc</a> file. To check a given python file, it suffices to
  run:
</p>

```bash
pylint <python_file>.py
```

<p align="justify">
  For an automated code formatting, one may also resort to <a href="https://github.com/psf/black">black</a> which is a very high efficient code
  formatter. Finally, the test of the modules can be performed using <a href="https://docs.pytest.org/en/6.2.x/">pytest</a>. The test files can
  be put inside the <a href="https://github.com/Radonirinaunimi/python-template/tree/master/tests">tests</a>. Then, to peform the tests, just run:
</p>

```bash
pytest <python_file>.py or pytest --cov=<package_name> tests/ (if you want to generare reports)
```


### Writing and building documentation 📘

<p align="justify">
  In order to adopt good practices for writing documentation, refer to the <a href="https://docs.python-guide.org/writing/documentation/">following</a>
  short guidelines. As default, this template uses <b>sphinx</b> as a python documentation tool which (for a local build) requires the installation of
  <b>sphinx</b> and <b>shpinx_rtd_theme</b>. For a deep dive into the sphinx tool, have a look at
  <a href="https://www.sphinx-doc.org/en/master/contents.html">this</a> documentation.
</p>
  
<p align="justify">
  In order to build the documentation in your local machine, go inside the 
  <a href="https://github.com/Radonirinaunimi/python-template/tree/master/doc">doc</a> folder and run the following command:
</p>

```bash
make html
```
<p> and to view the rendered document, just run: </p>

```bash
make view
```

### Tagging versions 🎉

<p align="justify">
  Semantic versioning is an important part in building packages. For the best practices in tagging versions, refer to the following
  <a href="https://semver.org/">documentation</a>. As a version management tool, this templates uses <b>bump2version</b> whose configuration
  file is defined in .bumpversion.cfg. The current version is <b>0.1.0-dev</b>, and in order to update if, run the following command:
</p>

```bash
bump2version minor # or major
```

For more details about the configuration of bump2version, head on to this <a href="https://github.com/c4urself/bump2version">github repository</a>.


## Automating pipeline with github actions

<p align="justify">
  Before pushing to the github , make sure to modify the actions in the 
  <a href="https://github.com/Radonirinaunimi/python-template/blob/master/.github/workflows/">workflows</a> folder. Specifically, one must replace 
  the value <b>never</b> in the <b>branches</b> entry. For instance, one can choose <b>on: push</b> to run the actions whenever a new implementation 
  is pushed on any <b>branches</b>.
</p>

<p align="justify">
  In order to deploy the documentation, the GITHUB_SECRETS must be replaced by your own <b>secrets</b>,
</p> 

```yaml
    - name: Deploy 🚀
      ...
        ACCESS_TOKEN: ${{ secrets.GITHUB_SECRETS }}
```

<p align="justify">
  Check this <a href="https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token">documentation</a> to learn how 
  to generate github-tokens, and the <a href="https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets">
  following</a> on how to add tokens to <b>secrets</b>. The <b>PyPI token</b> has to be generated from 
  <a href="https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/">here</a> by creating and
  account and added to the repository in the same way as for the documentation. Similarly, the <b>Codecov token</b> can be generated from 
  <a href="https://codecov.io/gh">here</a> for a specific repository.
</p>


## Useful links

<table>
  <tr>
    <td> Awesome python </td>
    <td> <a href="https://github.com/vinta/awesome-python">github</a> | <a href="https://awesome-python.com/)">webpage</a> </td>
  </tr>
  <tr>
    <td> All algorithms implemented in python </td>
    <td> <a href="https://github.com/TheAlgorithms/Python">github</a> </td>
  </tr>
  <tr>
    <td> PyGithub: Typed interactions with the GitHub API v3 </td>
    <td> <a href="https://github.com/PyGithub/PyGithub">github</a> | <a href="https://pygithub.readthedocs.io/">webpage</a> </td>
  </tr>
</table>


## Projects using this template

With **v.0.0.1** (as a proof of concept):
<table>
  <tr>
    <td> <b>Package</b> </td>
    <td> <b>Description</b>  </td>
  </tr>
  <tr>
    <td> <a href="https://github.com/Radonirinaunimi/Style-Transfer">Timst</b> </td>
    <td> Image style transfer using pyTorch. </td>
  </tr>
  <tr>
    <td> <a href="https://github.com/Radonirinaunimi/pwnd-check">CheckPwd</b> </td>
    <td> Python package that checks if your credentials have been leaked to the web. </td>
  </tr>
</table>
