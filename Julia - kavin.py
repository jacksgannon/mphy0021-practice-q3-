
def generate_data(resolution,zx,zy):
    initial_cond=True
    while initial_cond==True:
        zx_squared=zx*zx
        zy_squared=zy*zy
        if zx_squared+zy_squared>=4 or resolution<=1:
            initial_cond=False
        a=zx_squared-zy_squared-0.7
        zy=2.0*zx*zy+0.27015
        zx=a
        resolution -= 1

    A[y][x]=resolution

def main(y_axis_lim,x_axis_lim,resolution):
    A = np.zeros([y_axis_lim,x_axis_lim])    
    for x_point in range(x_axis_lim):
        for y_point in range(y_axis_lim):
            zx=1.5*(x-x_axis_lim/2)/(0.5*x_axis_lim)
            zy=1.0*(y-y_axis_lim/2)/(0.5*y_axis_lim)
            
            generate_data(resolution,zx,zy)
        
def plot_data(y_axis_lim,x_axis_lim,resolution):
    main(y_axis_lim,x_axis_lim,resolution)
    plt.imshow(A)
    plt.savefig('Myplot.png') #the order matters
    plt.show()
    

y_axis_lim=600
x_axis_lim=800
resolution=225
    
plot_data(y_axis_lim,x_axis_lim,resolution)