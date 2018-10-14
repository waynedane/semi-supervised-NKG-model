import torch 
import torch.nn.functional as F
def cosinesim(keyphrases, text):
  text = text.repeat(len(keyphrases))
  return F.cosine_similarity(keyphrase,text, dim=1,eps=1e-06)
  
