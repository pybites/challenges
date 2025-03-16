def hang_graphics():
    """Graphs from https://gist.github.com/DevDarren/4199441"""
    yield """
	________      
	|      |      
	|             
	|             
	|             
	|"""
    yield """
	________      
	|      |      
	|      0      
	|             
	|            
	|"""
    yield """
	________      
	|      |      
	|      0     
	|     /       
	|             
	|"""
    yield """

	|      |      
	|      0     
	|     /|      
	|             
	|"""
    yield """
	________      
	|      |      
	|      0      
	|     /|\     
	|             
	|"""
    yield """
	________      
	|      |      
	|      0      
	|     /|\     
	|     /       
	|"""
    yield """
	________      
	|      |      
	|      0      
	|     /|\     
	|     / \     
	|"""


if __name__ == '__main__':
    graphics = list(hang_graphics())
    print(len(graphics))
