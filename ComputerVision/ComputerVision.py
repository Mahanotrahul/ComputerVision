from PIL import Image
from pylab import *
from math import radians

image_location = "G:\Campus clix\main-gate.jpg"
#f = array(Image.open('H:\Vasitars.com\Logo\logo.png'))
#imshow(f)

def plt_save():
    plt.interactive(False)
    #x = np.arange(0, radians(1800), radians(12))
    #plt.plot(x, np.cos(x), 'b')
    x = range(6)
    #x = np.arange(1,5)
    plt.plot(x , [xi/3 for xi in x], label='Fast')
    plt.plot([0,1,5,10], label='Normal')
    plt.grid(True)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Plot')
    plt.legend()
    plt.show();
    M = np.array([[1,2,3],[4,5,6]])
    print(M[1,0])
    print(range(6))
    print(np.arange(6))
    plt.savefig('plot.png')

    plt.interactive(False)
    
    y = np.random.randn(1000)
    plt.hist(y)
    plt.show()



def interactivewindow():
    import matplotlib as mpl
    mpl.use('GTKAgg')   # to use GTK UI
    plt.plot([1,2,3,4])
    plt.show()



def image_points_and_lines():
    f = array(Image.open(image_location))
    imshow(f)


    x = [100,100,400,400]
    y = [200,500,200,500]


    plot(x,y,'r*')  # plot points with red-star marks

    plot(x[:2],y[:2])   #plot  line connecting first two points

    axis('off')     #hides the axis


    title('Image: Main Gate')
    show()

#image_points_and_lines()

def image_contours():
    f = array(Image.open('G:\Campus clix\main-gate.jpg').convert('L'))
    title('Converted Image')
    imshow(f)

    figure()    #create a new figure

    gray()      #don't use colours

    contour(f,origin = 'image')     # show contours with origin upper left corner
    
    axis('off')
    title('Contour Image')
    show()

#image_contours()

def image_histogram():
    
    f = array(Image.open(image_location).convert('L'))
    imshow(f)

    figure()
    hist(f.flatten(),128)       # flattened because hist() takes a one-dimensional array as input. flatten() converts any array to a one-dimensional array with values taken row-wise. Second argument is the number of bins to use.

    show()

#image_histogram()

def interactive_annotation():
    f = array(Image.open(image_location))
    title('Original Image')
    imshow(f)

    print('Click Three points on the image')
    x = ginput(3)
    print('You clicked: ' , x)
    show()



#interactive_annotation()


def image_shape_dtype():
    f = array(Image.open(image_location))
    title('Original Image')
    imshow(f)
    print(f.shape,f.dtype)

    im = f = array(Image.open(image_location),'f')
    title('Grayscale Image')
    imshow(im)

    
    print(im.shape,im.dtype)
    show()
#image_shape_dtype()

def invert_image():
    f = array(Image.open(image_location))
    figure()
    title('Original Image')
    imshow(f)
    print 'Original Image', int(f.min()), int(f.max())

    f1 = 255 - f
    

    figure()
    title('Inverted Image')
    imshow(f1)
    print 'Inverted Image', int(f1.min()), int(f1.max())
    
    f2 = f
    figure()
    title('Edited Image')
    imshow(f2)
    print 'Edited Image', int(f2.min()), int(f2.max())
    show()

invert_image()