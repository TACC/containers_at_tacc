Contributing
============

Usual git flow of issues -> branches -> PRs -> approve -> merge.

To build these docs locally:
----------------------------

Clone the repository and enter the root directory. Then switch to a new branch, make changes, etc.

Then build the site locally to see how your changes look.

First create a python environment for the dependancies:

.. code-block:: console
    python3 -m venv readthedocs
    source ./readthedocs/bin/activate
    python -m pip install --upgrade --no-cache-dir pip setuptools
    python -m pip install --upgrade --no-cache-dir sphinx readthedocs-sphinx-ext
    python -m pip install --exists-action=w --no-cache-dir -r docs/requirements.txt
    deactivate

You only need to make the environment once.

When you want to build the site, activate the environment and then run Sphinx.

.. code-block:: console
    source ./readthedocs/bin/activate
    cd docs
    python -m sphinx -T -b html -d _build/doctrees -D language=en . ../local
    open ../local/index.html

For some changes you may want to clear the old site data first.

.. code-block:: console
    rm -rf ../local ./_build

When you're happy with your changes, make a PR for your branch.