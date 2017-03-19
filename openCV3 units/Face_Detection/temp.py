import cv2, time

def read_images(path, sz=None):

    c = 0
    X, y = [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                try:
                    if(filenames == ".directory"):
                        continue
                    filepath = os.path.join(subject_path, filename)
                    im = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

                    # resize to given size (if given)
                    if (sz is not None):
                        im = cv2.resize(im, (200, 200))

                    X.append(np.asarray(im, dtype=np.unit8))
                    y.append(c)
                except IOError, (errno, strerror):
                    print "I/O error({0}):{1}".format(errno, strerror)
                except:
                    print ('Unexpected error:', sys.exc_info()[0])
                    raise
            c = c+1

    return [X,y]

def face_rec():
    names = ["Joe", "Jane", "Jack"]
    if len(sys.argv) < 2:
        print("USAGE: facered_demo.py </path/to/image> [</path/to/store/images/at>]")
        sys.exit()
 
    [X,y] = 
