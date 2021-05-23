import numpy as np

class scrabble_bag:
    def __init__(self, num_players, seed):
        #np.random.state = random_seed
        #np.random.seed(random_seed)
        #self.players = players
        
        self.num_players = num_players
        self.bag_contents = ['E'] * 15 + ['N'] * 9 + ['S'] * 7 + ['I', 'R', 'T', 'U'] * 6 + ['A'] * 5 + ['D', 'H', 'M'] * 4 + ['G', 'L', 'O'] * 3 + ['Joker', 'B', 'C', 'F', 'K'] * 2 + ['W', 'Z', 'P', 'Ä', 'J', 'Ü', 'V', 'Ö', 'X', 'Q', 'Y']
        self.round = 0
        self.turn = 0
        self.rng = np.random.default_rng(seed)
        #self.start_player = players[rng.choice(self.num_players, size = 1)[0]]
        #return self.turn
    
    def __len__(self):
        return len(self.bag_contents)
    
    def what_round(self):
        #use this to determine whether show = False
        return self.turn // self.num_players + 1
    
    
    def remove(self, num_letters, show = False):

        inds_remove = list(self.rng.choice(len(self.bag_contents), size=num_letters, replace=False))
        inds_remain = [num for num in range(len(self.bag_contents)) if num not in inds_remove]
        
        remove_l = [self.bag_contents[i] for i in inds_remove]
        self.bag_contents = [self.bag_contents[i] for i in inds_remain]
        
        self.turn += 1
        
        if (show):
            return remove_l
        else:
            return "Not your turn"
    
    def put_back(self, letters):
        self.bag_contents += letters
        return self.remove(len(letters))
    