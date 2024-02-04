Unitest - Unit testing framework
Source code: Lib/unittest/__init__.py

(If you are already familiar with the basic concepts of testing, you might want to skip to the list of assert methods.)

The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

To achieve this, unittest supports some important concepts in an object-oriented way:

test fixture
A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

test case
A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.

test suite
A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.

test runner
A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.

See also
Module doctest
Another test-support module with a very different flavor.

Simple Smalltalk Testing: With Patterns
Kent Beck’s original paper on testing frameworks using the pattern shared by unittest.

pytest
Third-party unittest framework with a lighter-weight syntax for writing tests. For example, assert func(10) == 42.

The Python Testing Tools Taxonomy
An extensive list of Python testing tools including functional testing frameworks and mock object libraries.

Testing in Python Mailing List
A special-interest-group for discussion of testing, and testing tools, in Python.

The script Tools/unittestgui/unittestgui.py in the Python source distribution is a GUI tool for test discovery and execution. This is intended largely for ease of use for those new to unit testing. For production environments it is recommended that tests be driven by a continuous integration system such as Buildbot, Jenkins, GitHub Actions, or AppVeyor.
