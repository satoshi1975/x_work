from django.test import TestCase, RequestFactory, Client
from django.shortcuts import get_object_or_404
from employers.models import Employer, Vacancy
from main.models import User,Cities
from django.urls import reverse
from employers.views import CVSearchView
from job_seekers.models import CV,JobSeeker

class CreateVacancyTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gos.com', password='testpassword', username='testuser')
        self.employer = Employer.objects.create(user=self.user,company_name='testcompany')
        self.create_vacancy_url= reverse('create_vacancy',kwargs={'user_id':self.user.id})
        self.city= Cities.objects.create(city='New York',state_name='New York')
    def test_create_vacancy_success(self):
        self.client.force_login(self.user)
        data={
            'occupation':'engineer',
            'job_description':'some info',
            'education':'bachelor',
            'schedule':'flex',
            'work_place':'flex',
            'city_id':self.city.id,
            'experience':'1',
            'salary':'12000',
            'key_skills':'None, null',
        }
        response = self.client.post(self.create_vacancy_url,data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('vacancy_list',kwargs={'user_id':self.user.id}))
        self.assertEqual(Vacancy.objects.filter(occupation='engineer').exists(),
                        True)
        
    def test_create_vacancy_failure(self):
        self.client.force_login(self.user)
        data={
            'occupation':'engineer2',
            'job_description':'another info',
            'education':'none',
            'schedule':'full',
            'work_place':'full',
            'city_id':self.city.id,
            'experience':'1',
            'salary':'12000g',
            'key_skills':'None, null',
        }
        response = self.client.post(self.create_vacancy_url,data=data)
        self.assertEqual(response.status_code, 302)
        
        self.assertRedirects(response, reverse('vacancy_list',kwargs={'user_id':self.user.id}))
        self.assertEqual(Vacancy.objects.filter(occupation='engineer2').exists(),
                        False)

class EditVacancyTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gos.com', password='testpassword', username='testuser')
        self.employer = Employer.objects.create(user=self.user,company_name='testcompany')
        self.city= Cities.objects.create(city='New York',state_name='New York')
        self.vacancy=Vacancy.objects.create(employer=self.employer,
                                            city=self.city,
                                            occupation='fakeoccupation',
                                            schedule='none',
                                            experience=2,
                                            education='none',
                                            salary='19000',
                                            work_place='full',
                                            job_description='some info',
                                            key_skills='someinfo')
        self.edit_vacancy_url= reverse('edit_vacancy',kwargs={'vacancy_id':self.vacancy.id})
        self.client.force_login(self.user)
    
    def test_edit_vacancy_success(self):
        
        new_data = {
            'city_id':self.city.id,
            'occupation':'newoccupation',
            'schedule':'full',
            'experience':'1',
            'education':'none',
            'salary':20000,
            'work_place':'full',
            'job_description':'anotherdesc',
            'key_skills':'anotherskills',
        }
        response=self.client.post(reverse('edit_vacancy',kwargs={'vacancy_id':self.vacancy.id}),data=new_data)
        
        self.assertNotEqual(self.vacancy.occupation, Vacancy.objects.get(employer=self.employer).occupation)
    def test_edit_vacancy_failure(self):
        
        new_data = {
            'city_id':self.city.id,
            'occupation':'newoccupation',
            'schedule':'full sss',
            'experience':'1',
            'education':'none',
            'salary':20000,
            'work_place':'full',
            'job_description':'anotherdesc',
            'key_skills':'anotherskills',
        }
        response=self.client.post(reverse('edit_vacancy',kwargs={'vacancy_id':self.vacancy.id}),data=new_data)
        
        self.assertEqual(self.vacancy.occupation, Vacancy.objects.get(employer=self.employer).occupation)

class CVSearchViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(email='testuser@gos.com', password='testpassword', username='testuser')
        self.city=Cities.objects.create(city='New York',state_name='New York')
        self.jobseeker=JobSeeker.objects.create(user=self.user,first_name='name',last_name='name',
                                                email='email@test.com',city=self.city)
        self.city2=Cities.objects.create(city='San Francisco',state_name='Florida')
    
    def test_cv_search(self):
        # Создание тестовых данных
        CV.objects.create(jobseeker=self.jobseeker,occupation='Software Engineer', city=self.city,
                        experience=3, schedule='full',work_place='full',salary=50000,education='bachelor')
        CV.objects.create(jobseeker=self.jobseeker,occupation='Web Developer', city=self.city2,
                        experience=5, schedule='full',work_place='none',salary=100000,education='master')
        
        url = reverse('search_cv')
        data = {
            'occupation': 'Engineer',
            'city_id': self.city.id,
            'experience': '1|5',
            'schedule': 'full',
            'education': 'bachelor',
            'salary': 50000,
            'work_place': 'full',
        }
        request = self.factory.get(url, data)
        
        response = CVSearchView.as_view()(request)
        
        # Проверка, что код ответа равен 200 (успех)
        self.assertEqual(response.status_code, 200)
        
        # Проверка контекста
        context = response.context_data
        print('CONTEXT')
        print(context)
        self.assertEqual(context['occupation'], 'Engineer')
        self.assertEqual(context['city_id'], '1')
        self.assertEqual(context['experience'], '1|5')
        self.assertEqual(context['schedule'], 'full')
        self.assertEqual(context['education'], 'bachelor')
        self.assertEqual(context['salary'], '50000')
        self.assertEqual(context['work_place'], 'full')
        
        # Проверка queryset
        queryset = context['cv']
        self.assertEqual(len(queryset), 1)
        self.assertEqual(queryset[0].occupation, 'Software Engineer')
        self.assertEqual(queryset[0].city, self.city)
        self.assertEqual(queryset[0].experience, 3)
        self.assertEqual(queryset[0].schedule, 'full')