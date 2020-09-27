

cng_msg = 'Dont change the properties of class.'
sld_work = 'Function overloading should work.'

#class Meta(type):

@test.describe('Python Recipes #1 : Function Overloading')
def _():
    # implement meta class -----

    def build():  # returning class to regenerate accordingly.

        class Overload(metaclass=Meta):
            CLS_VAR = 42

            def __init__(self):
                self.a = 1
                self.no = 'This is "No parameter" function.'
                self.single = 'This is "Single parameter" function'
                self.two = 'This is "Two parameter" function'
                self.three = 'This is "Three parameter" function'

            def foo(self):
                return self.no

            def foo(self, x):
                return self.single + ':' + str(x)

            def foo(self, x, y):
                return self.two + ':' + str(x) + ',' + str(y)

            def foo(self, x, y, z):
                return self.three + ':' + str(x) + ',' + str(y) + ',' + str(z)

            def extra(self):
                return 'This is extra method.'

        return Overload

    @test.describe('Sample tests')
    def _():
        overload = build()
        obj = overload()

        @test.it('Verifying access')
        def _():
            test.assert_equals(obj.a, 1, cng_msg)
            test.assert_equals(obj.no, 'This is "No parameter" function.', cng_msg)
            test.assert_equals(obj.single, 'This is "Single parameter" function', cng_msg)
            test.assert_equals(obj.two, 'This is "Two parameter" function', cng_msg)
            test.assert_equals(obj.three, 'This is "Three parameter" function', cng_msg)
            test.assert_equals(obj.extra(), 'This is extra method.', cng_msg)
            test.assert_equals(obj.CLS_VAR, 42, cng_msg)

        @test.it('Verifying overloading feature')
        def _():
            test.assert_equals(obj.foo(), 'This is "No parameter" function.', sld_work)
            test.assert_equals(obj.foo(1), 'This is "Single parameter" function:1', sld_work)
            test.assert_equals(obj.foo(1, 2), 'This is "Two parameter" function:1,2', sld_work)
            test.assert_equals(obj.foo(1, 2, 3), 'This is "Three parameter" function:1,2,3', sld_work)

        @test.it('Verifying overloading feature after adding new methods :1')
        def _():
            def foo(self, a, b, c, d):
                return self.a + a + b + c + d

            def foo1(self, a, b):
                return 'Overwritten'

            overload.foo = foo

            test.assert_equals(obj.foo(), 'This is "No parameter" function.', sld_work)
            test.assert_equals(obj.foo(1), 'This is "Single parameter" function:1', sld_work)
            test.assert_equals(obj.foo(1, 2), 'This is "Two parameter" function:1,2', sld_work)
            test.assert_equals(obj.foo(1, 2, 3), 'This is "Three parameter" function:1,2,3', sld_work)

            test.assert_equals(obj.foo(1, 2, 3, 4), 11, sld_work)

            overload.foo = foo1
            test.assert_equals(obj.foo(1, 2), 'Overwritten', sld_work)

        @test.it('Verifying overloading feature after adding new methods :2')
        def _():
            def boo1(self):
                return self.a

            def boo2(self, a):
                return self.a + a

            def unique(self, a, b):
                return a + b

            overload.boo = boo1
            overload.boo = boo2
            obj.nothing = '123'
            overload.unique = unique

            test.assert_equals(obj.boo(), 1, sld_work)
            test.assert_equals(obj.boo(1), 2, sld_work)
            test.assert_equals(obj.unique(1, 2), 3, sld_work)
            test.assert_equals(obj.nothing, '123', sld_work)

        @test.describe('Verify the absence of unwanted sharing of methods between different classes')
        def _():
            class Unshare(metaclass=Meta):
                def foo(self, a, b): return 'unshared!'

            unsh = Unshare()

            @test.it('The new foo function in Unshare class should be used')
            def _():
                test.assert_equals(unsh.foo(1, 2), 'unshared!')

            @test.it(
                'Previous implementations of "foo" in other classes shouldn\'t be visible from a freshly built class')
            def _():
                test.expect_error("Your function didn't raise any exception", lambda: unsh.foo(1), Exception)
                test.expect_error("Your function should raise AttributeError", lambda: unsh.foo(1), AttributeError)

            @test.it('Previous method with the same signature in other classes shouldn\'t be affected')
            def _():
                test.assert_equals(obj.foo(1, 2), 'Overwritten')

        @test.it('Class level variables are still working as expected')
        def _():
            def over():  obj.CLS_VAR = -42

            def write(): obj.HAHA = msg

            test.expect_no_error("Class level variables can be overriden", over)
            test.assert_equals(obj.CLS_VAR, -42, "Class variable Overload.CLS_VAR hasn't been overriden")

            msg = 'This is another class variable'
            test.expect_no_error("New class level variables can be defined", write)
            test.assert_equals(obj.HAHA, msg, "New class level variables can be defined and accessed")

        @test.it('Undefined methods or variables should raise AttributeError')
        def _():
            test.expect_error('Undefined attributes/mehtods should raise AttributeError',
                              lambda: overload.NEW_CLS_VAR, AttributeError)
            test.expect_error('Undefined attributes/mehtods should raise AttributeError',
                              lambda: obj.ABCD, AttributeError)
            test.expect_error('Undefined attributes/mehtods should raise AttributeError',
                              lambda: obj.randomFuncName(), AttributeError)

        @test.it('undefined overloaded methods (wrong number of arguments should raise AttributeError)')
        def _():
            test.expect_error('Undefined attributes/mehtods should raise AttributeError',
                              lambda: overload.foo(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), AttributeError)
