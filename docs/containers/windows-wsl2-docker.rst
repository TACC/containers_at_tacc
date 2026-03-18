:orphan:

.. _windows-wsl2-docker:

Windows: Installing WSL2 and Docker Desktop
===========================================

Windows users should install WSL2 (Windows Subsystem for Linux 2) before
installing Docker Desktop. WSL2 provides a full Linux kernel running inside
Windows and is the recommended backend for Docker Desktop on Windows.

Step 1 — Enable WSL2
---------------------

Open PowerShell or Windows Command Prompt as Administrator and run:

.. code-block:: console

   > wsl --install

This command enables the required Windows features, downloads the latest Linux
kernel, sets WSL2 as the default version, and installs Ubuntu as the default
Linux distribution. Restart your machine when prompted.

.. note::

   If you already have WSL installed, make sure WSL2 is set as the default
   version by running ``wsl --set-default-version 2``.

After rebooting, open the Ubuntu app from the Start menu to complete the
initial Linux user setup (create a username and password).

To confirm WSL2 is active, run the following in PowerShell:

.. code-block:: console

   > wsl --list --verbose
   NAME      STATE           VERSION
   * Ubuntu  Running         2

The ``VERSION`` column should show ``2`` for your distribution.

Step 2 — Install Docker Desktop
---------------------------------

#. Download Docker Desktop for Windows from
   `<https://docs.docker.com/desktop/install/windows-install/>`_.
#. Run the installer. When prompted, make sure "Use WSL 2 instead of
   Hyper-V" is checked.
#. After installation, launch Docker Desktop and go to
   Settings → Resources → WSL Integration.
#. Enable integration for your Ubuntu distribution (or whichever distro you
   installed in Step 1) and click Apply & Restart.

.. note::

   Docker Desktop must be running in the system tray before you can use Docker
   commands in your terminal.

Step 3 — Open a WSL2 Terminal
-------------------------------

All Docker commands in this tutorial should be run inside your WSL2 terminal
(Ubuntu), not in PowerShell or CMD. You can open it by:

- Launching the Ubuntu app from the Start menu, or
- Opening Windows Terminal and selecting the Ubuntu profile from the
  dropdown.

Step 4 — Verify the Installation
----------------------------------

In your WSL2 Ubuntu terminal, run:

.. code-block:: console

   $ docker version

You should see output showing both a Client and Server version. You can also
run a quick smoke test:

.. code-block:: console

   $ docker run hello-world

   Hello from Docker!
   This message shows that your installation appears to be working correctly.

If both commands succeed, your WSL2 and Docker Desktop setup is complete. You can now run Docker commands in your WSL2 terminal or use the terminal in the Docker Desktop app.