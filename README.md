# Linear-Colour-Transfer
Simple, effective colour transfer using linear algebra. Supports arbitrary image masking for selective transfer.

* Given a source image (reference) and a target image (image to be recolored) this repo performs fast linear colour transfer based on similarity transform in RGB vector space.
* based upon the histogram matching method outlined in Gatys, Leon A., et al., "Controlling perceptual factors in neural style transfer." IEEE Conference on Computer Vision and Pattern Recognition (CVPR). 2017."
* Code is adapted from and extends the code in the repo of https://github.com/ProGamerGov/Neural-Tools.git.
* The primary extension is that now colour can be arbitrarily sampled from a reference image using binary masking and applied selectively to a target image also using binary masking (see examples). 
* This method is much more stable than simple matching of mean and standard deviation (see baseline example comparison). 

## Examples

*Baseline Example*
![baseline_example](https://github.com/fyz11/Linear-Colour-Transfer/blob/master/results/baseline.png)

*Example 1: Full colour transfer based on a reference image*
![example_1](https://github.com/fyz11/Linear-Colour-Transfer/blob/master/results/example1.png)

*Example 2: Selective recoloring using image masking on the target image*
![example_1](https://github.com/fyz11/Linear-Colour-Transfer/blob/master/results/example2.png)

*Example 3: Selective color sampling from reference image and selective recoloring on the target image* 
![example_1](https://github.com/fyz11/Linear-Colour-Transfer/blob/master/results/example3.png)
