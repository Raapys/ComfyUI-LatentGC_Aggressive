import torch
import comfy.model_management as mm
import gc

class LatentGC_Aggressive:
    def __init__(self):
        pass
    
    @classmethod
    
    def INPUT_TYPES(s):
      return {
        "required": {
			  "samples": ("LATENT",),
		  }
	  }
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "tunnelLatents"
    CATEGORY = "latent"

    def tunnelLatents(self, samples):
        s = samples.copy()
        gc.collect()
        mm.unload_all_models()
        mm.soft_empty_cache()
        return (s,)
      
NODE_CLASS_MAPPINGS = {
	"LatentGC": LatentGC_Aggressive,
}
