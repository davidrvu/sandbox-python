from plotly import __version__
from plotly.graph_objs import Scatter, Figure, Layout, Scattergl
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd


def plotFunc(debug, fileOut, titlePlot, ejeX, ejeY_experim, ejeY_teorico):

    markerSize = 5
    lineWidth  = 3

    smooth1    = 0.0
    smooth2    = 0.05
    smooth3    = 0.1
    smooth4    = 1.0
    smooth5    = 1.3

    colorTrace1 = 'rgba( 68, 114, 196, 1.0)' 
    colorTrace2 = 'rgba(237, 125,  49, 1.0)'
    colorTrace3 = 'rgba(0, 200,  200, 1.0)'
    colorTrace4 = 'rgba(0, 0,  0, 1.0)'
    colorTrace5 = 'rgba(0, 200,  100, 1.0)'

    trace1 = Scatter(
                        x=ejeX, 
                        y=ejeY_experim, 
                        mode       = 'lines+markers',
                        name       = 'spline ' + str(smooth1),
                        line   = dict(
                                        shape     = 'spline',
                                        smoothing = smooth1 
                                     ),
                        marker = dict(
                                        size = markerSize,
                                        color = colorTrace1,
                                        line = dict(
                                                    width     = lineWidth,
                                                    color     = colorTrace1                                                
                                                    )
                                      )
                    )

    trace2 = Scatter(
                        x=ejeX, 
                        y=ejeY_experim, 
                        mode = 'lines+markers',
                        name       = 'spline ' + str(smooth2),
                        line   = dict(
                                        shape     = 'spline',
                                        smoothing = smooth2 
                                     ),
                        marker = dict(
                                        size = markerSize,
                                        color = colorTrace2,
                                        line = dict(
                                                    width     = lineWidth,
                                                    color     = colorTrace2
                                                    )
                                      )                        
                    )

    trace3 = Scatter(
                        x=ejeX, 
                        y=ejeY_experim, 
                        mode = 'lines+markers',
                        name       = 'spline ' + str(smooth3),
                        line   = dict(
                                        shape     = 'spline',
                                        smoothing = smooth3 
                                     ),
                        marker = dict(
                                        size = markerSize,
                                        color = colorTrace3,
                                        line = dict(
                                                    width     = lineWidth,
                                                    color     = colorTrace3
                                                    )
                                      )                        
                    )

    trace4 = Scatter(
                        x=ejeX, 
                        y=ejeY_experim, 
                        mode = 'lines+markers',
                        name       = 'spline ' + str(smooth4),
                        line   = dict(
                                        shape     = 'spline',
                                        smoothing = smooth4 
                                     ),
                        marker = dict(
                                        size = markerSize,
                                        color = colorTrace4,
                                        line = dict(
                                                    width     = lineWidth,
                                                    color     = colorTrace4
                                                    )
                                      )                        
                    )

    trace5 = Scatter(
                        x=ejeX, 
                        y=ejeY_experim, 
                        mode = 'lines+markers',
                        name       = 'spline ' + str(smooth5),
                        line   = dict(
                                        shape     = 'spline',
                                        smoothing = smooth5 
                                     ),
                        marker = dict(
                                        size = markerSize,
                                        color = colorTrace5,
                                        line = dict(
                                                    width     = lineWidth,
                                                    color     = colorTrace5
                                                    )
                                      )                        
                    )

    data  = [trace1, trace2, trace3, trace4, trace5]

    layout = Layout(
        legend = dict(
                        orientation="v",  #"h"
                        #x=0.6,
                        #y=0.1
                     ),
        title  = titlePlot,
        titlefont=dict(
                        #family='Courier New, monospace',
                        #size=18,
                        color='#000000' #BLACK
                      ),
        xaxis=dict(
            title = "X AXIS",
            titlefont=dict(
                #family='Courier New, monospace',
                size=16,
                color='#000000' #BLACK
              ),
            autorange=True,
            showgrid=True
        ),
        yaxis=dict(
            title = "Y AXIS", # PLOTLY WITH LATEX
            titlefont=dict(
                #family='Courier New, monospace',
                size=16,
                color='#000000' #BLACK
              ),
            autorange=True,
            showgrid=True
        )
    )

    fig = dict(data = data, layout = layout)
    plot(fig, filename=fileOut + ".html", auto_open=True, image='png', image_filename = fileOut)

def main():
    #######################################
    ## PARAMETERS
    #######################################
    fileIn    = "ejemplo2.csv"
    fileOut   = "testing_version"
    titlePlot = "<b>Testing Version</b> <br> Example 1" 
    debug     = 1

    #######################################
    ## READ DATA
    #######################################
    try:
        dataIn = pd.read_csv(fileIn,
                            sep = ',',
                            header = 0,
                            index_col = False,
                            engine = 'c',
                            na_values = 'nan',
                            keep_default_na=False,
                            na_filter= False,
                            memory_map = True
                            )
    except IOError:
        eprint("\nERROR: The input file " + fileIn + " does not exist.")
        sys.exit()


    ejeX         = dataIn["ejeX"].values.tolist()
    ejeY_experim = dataIn["ejeY2"].values.tolist()
    ejeY_teorico = dataIn["ejeY2"].values.tolist()


    #######################################
    ## PLOT
    #######################################
    plotFunc(debug, fileOut, titlePlot, ejeX, ejeY_experim, ejeY_teorico)

    print("DONE!")


if __name__ == "__main__":
    main()