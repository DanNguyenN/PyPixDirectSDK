function IRInterface = init()
    % initialize the interface as a global variable
    IRInterface = EvoIRMatlabInterface;
    IRInterface.connect()