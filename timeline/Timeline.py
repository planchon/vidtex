# coding: utf-8

class Timeline(object):
    timeline_object = []
    timeline        = []

    max_id = 0
    last_time_index = 0
    
    def __init__(self):
        pass

    # ajoute un element dans la timeline retourne la timeline_id de lobject
    # prend des frames comme unite de mesure du temps
    def add_object(self, animation, start, end, position):
        animation_id = self.get_global_id()
        self.timeline_object[animation_id] = animation                      # retourne l'id unique de l'anim
        self.add_into_timeline(start, [start, end, position, animation_id]) # permet d'ajouter dans la liste triée
        
        return animation_id
        
    # retourne toutes les animation a faire au temps t
    # retourne une liste d'id
    def get_all_animation_at(self, t):
        animation_to_render = []
        not_finished = True
        tmp_time = self.last_time_index
        
        while not_finished and (tmp_time < len(self.timeline)):
            if (self.timeline[tmp_time, 0] < t) and (self.timeline[tmp_time, 1] > t):
                # on ajoute l'id et la position dans la frame de l'animation
                animation_to_render.append([self.timeline[tmp_time, 3], self.timeline[tmp_time, 2]]) 
                # dans le cas ou l'animation se termine
            if (self.timeline[tmp_time, 1] < t) and (self.timeline[tmp_time, 0] < t):
                tmp_time += 1
            if (self.timeline[tmp_time, 0] > t):
                self.last_time_index = tmp_time
                not_finished = False

        return animation_to_render
                    

    # retourne la place de l'animation dans la timeline
    def dichotomic_search(start):
        l = 0
        r = len(self.timeline) // 2
        
        def dicho(l, r):
            m = (l + r) // 2
            if (start <= self.timeline[r, 0]) and (start >= self.timeline[l, 0]):
                return l
            if start > self.timeline[r, 0]:
                dicho(r, r + m)
            else:
                dicho(m, r)

        return dicho(l, r)

    # ajoute le tuple [start, end, position, animation_id] dans la timeline
    def add_into_timeline(self, start, element):
        index = dichotomic_search(start)
        self.timeline.insert(index, element)

    # retourne le prochain id utilisable
    def get_global_id(self):
        self.max_id = self.max_id + 1
        return str(self.max_id)
    
    # enelve une animation de la timeline
    def remove_animation(self, id):
        pass
