def Renders(this):
    def wrap_func():
        print(f'The wrapped function returned {this()}')
    return wrap_func

@Renders
def newfunc():
    return '<h1>Hello World</h1>'

newfunc()