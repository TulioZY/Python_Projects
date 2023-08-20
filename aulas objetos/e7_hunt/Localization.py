import win32gui

def callback(hwnd, x):
    global X, Y, W, H
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    if win32gui.GetWindowText(hwnd) == "LDPlayer":
        X = x
        Y = y - 33
        W = w + 30 
        H = h - 90
def main():
    global X, Y, W, H
    win32gui.EnumWindows(callback, None)
    return(X,Y,W,H)
if __name__ == '__main__':
    main()