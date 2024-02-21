function [RGB, THM] = capture()
    global IRInterface
    if isempty(IRInterface)
        IRInterface = EvoIRMatlabInterface;
        IRInterface.connect()
        IRInterface.set_palette_manual_temp_range(25,30);
    end
    RGB = IRInterface.get_palette();        % grab palette image
    THM = IRInterface.get_thermal();        % grab thermal image
end