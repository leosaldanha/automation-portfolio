## Front-end test cases

### Introduction

This section aims to display different web automation frameworks.

The website chosen to be automated is [automationpractice.com](http://automationpractice.com/index.php) since it was developed specifically for this purpose.

Note: _For now_ I will not be including mobile automation, but in the future I plan to.

### Test cases

Let's name the user as Luke. :)

#### SEARCH

| \#  | Test scenario                 | Step by step                                                                                                                                                                                              |
| --- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Search for a valid product    | **Given** Luke is at the Home page<br>**When** he searches for a valid product (e.g. "shirt")<br>**Then** he must be redirected to the results page<br>And it must display coherent results               |
| 2   | Search for an invalid product | **Given** Luke is at the Home page<br>**When** he searches for an invalid product (e.g. "abc")<br>**Then** he must be redirected to the Results page<br>And it must notify him that no results were found |
| 3   | Search for an empty value     | **Given** Luke is at the Home page<br>**When** he searches for an empty value<br>**Then** he must be redirected to the Results page<br>And it must require some text as input                             |