# browser_automation_py
Web automation on python.

### Setting up the env:

1. Install [Python](https://www.python.org)
   ```
   check: python3 --version
   ```
2. Configure python env:
   ```
   cd /usr/local/bin
   python3 -m venv ~/venvs/python310
   ```
3. Activate py env:
   ```
   source ~/venvs/python310/bin/activate
   ```
4. Install selenium:
   ```
   pip install selenium
   pip list
   ```
5. Download [chromedriver](https://chromedriver.chromium.org/)
6. Add the webdriver to your PATH environment variable:
   ```
   add a string in: .bashrc, bash_profile, .zshrc or .profile
   e.g.: export PATH=$PATH:~/drivers
   ```

### Check the selenium interacts the browser:
   ```
   python3
   from selenium import webdriver
   browser = webdriver.Chrome()
   browser.get('google.com')
   browser.close()
   ```
### Trigger the trial_of_the_stones.py:
   ```
   python -i ./tests/trial_of_the_stones.py 
   ```
   The "-i" flag allows you to interact your browser after the script is finished.