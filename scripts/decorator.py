try:
    wait = WebDriverWait(driver,5)
    wait.until(ec.visibility_of_element_located((By.Id, 'test')))
    print('iframe found')

except TimeoutException:
    print('there is no iframe')