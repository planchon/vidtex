import bisect
import inspect

class Timeline(object):    
    def __init__(self):
        self.timeline_object = {}
        self.timeline        = []
        self.timeline_index  = []
        self.max_id          = 0

    # ajoute un element dans la timeline retourne la timeline_id de l'object
    # prend des frames comme unité de mesure du temps
    def add_object(self, animation, start, end, position):
        animation_id = self.get_global_id()
        self.timeline_object[animation_id] = animation                      # retourne l'id unique de l'anim
        self.add_into_timeline(start, [start, end, position, animation_id]) # permet d'ajouter dans la liste triée
        return animation_id

    def get_timeline_objects(self):
        return self.timeline_object.items()
    
    # retourne toutes les animation a faire au temps t
    # retourne une liste d'id
    def get_all_animation_at(self, t):
        animation_to_render = []
        not_finished = True
        tmp_index = 0
        has_add = False
        
        while not_finished and (tmp_index < len(self.timeline)):
            start = self.timeline[tmp_index][0]
            end   = self.timeline[tmp_index][1]
            has_add = False
            
            # c'est une animation qui convient
            if t >= start and t <= end:
                animation_to_render.append([self.timeline[tmp_index][3], self.timeline[tmp_index][2]])
                tmp_index += 1
            # on est sur des animations finies
            if t > end:
                tmp_index += 1
            # les animations sont triees, les prochaines commencent apres
            if t < start:
                not_finished = False
            
        return animation_to_render
                    
    # ajoute le tuple [start, end, position, animation_id] dans la timeline
    def add_into_timeline(self, start, element):
        index = bisect.bisect(self.timeline_index, start)
        self.timeline_index.insert(index, start)
        self.timeline.insert(index, element)

    # retourne le prochain id utilisable
    def get_global_id(self):
        self.max_id = self.max_id + 1
        return str(self.max_id)
    
    # enelve une animation de la timeline
    def remove_animation(self, id):
        pass
