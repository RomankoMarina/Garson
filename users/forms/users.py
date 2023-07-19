"""class CamForm(forms.ModelForm):
    class Meta:
        model = Cam
        fields = ('awis','title','ip','mac','gw','gw_type','switch','port','status','password','server','zone','goal')
        labels = {'awis':'Awis','title':'Название','ip':'IP','mac':'MAC',
                  'gw':'GateWay','gw_type':'Тип роутера',
                  'switch':'Свич','port':'port','status':'Статус','server':'Сервер','zone':'Зоны','goal':'Цель'}
        values = {"save": u'Добавить'}
        widgets = {
            'zone': forms.CheckboxSelectMultiple()}

"""