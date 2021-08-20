# WorkshopPythonRefactoring

To run your approval tests properly:
* run the tests from CodeSense or the Test Explorer
* in the terminal,
  * coverage erase
  * coverage run --branch -m pytest
  * coverage xml
  * Press Ctrl+Shift+7 to show Coverage (or click Watch in status bar)
  * Press Ctrl+Shift+9 to hide Coverage (or click No Coverage in status bar)