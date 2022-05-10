graph={
    'Al-Baramon':['Sherbeen','Sharmsah','Talkha','Mansoura'],
    'Al-Zarka':['Demyat','Sharmsah'],
    'Batra/Bsat':['Sherbeen','Talkha'],
    'Bila':['Tirah','Kafr El-Grayda'],
    'Dekernes':['Mit Elkholy','Shoha'],
    'El-Rahbeen':['Samanood','El-Mahala Elkubra'],
    'El-Mahala Elkubra':['El-Rahbeen','Nemra ElBasal','El-Sagay3a'],
    'El-Sagay3a':['El-Mahala Elkubra','Samatay'],
    'El-Gamalyiah':['Mit Salsil'],
    'Kafr El-Grayda':['Bila','Belqas'],
    'Kafr Demera':['Belqas','Talkha',"Nabaroh"],
    'Kafr Allam':['Mit Salsil','Mit Elkholy'],
    'Kafr ELShaikh':[],
    'Mansoura':['Talkha','Sandob','Shoha',"Al-Baramon","Batra/Bsat","Nabaroh","Samanood"],
    'Matbol':['Nemra ElBasal','Kafr ELShaikh'],
    'Mit Elkholy':['Kafr Allam','Dekernes'],
    'Mit Salsil':['El-Gamalyiah','Kafr Allam'],
    'Nabaroh':['Tirah','Talkha','Kafr Demera','Mansoura'],
    'Nemra ElBasal':['El-Mahala Elkubra',"Matbol",'Samatay'],
    'Qtor':['Samatay','Kafr ELShaikh'],
    'Sandob':['El-Senbelayain','Aga','Mansoura'],
    'Shoha':['Dekernes','Talkha','Al-Baramon','Mansoura'],
    'Samanood':['El-Rahbeen','Aga','Talkha','Mansoura'],
    'Samatay':['El-Sagay3a','Qtor','Nemra ElBasal'],
    'Sharmsah':['Al-Zarka',"Al-Baramon",'Sherbeen'],
    'Sherbeen':['Demyat','Sharmsah',"Batra/Bsat"'Al-Baramon'],
    'Talkha':['Nabaroh','Batra/Bsat','Kafr Demera','Samanood','Mansoura'],
    'Tirah':['Bila','Nabaroh'],
}
def bfs(graph,start,goal):
    visited = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node,[])
            for node2 in adjacent_nodes:
                new_path = path.copy()
                new_path.append(node2)
                queue.append(new_path)
                
