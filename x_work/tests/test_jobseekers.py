from django.test import TestCase, RequestFactory, Client
from django.shortcuts import get_object_or_404
from employers.models import Employer, Vacancy
from main.models import User,Cities
from django.urls import reverse
from job_seekers.views import VacancySearchView
from job_seekers.models import CV,JobSeeker
from datetime import date

class CreateCvTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gos.com', password='testpassword', username='testuser')
        # self.employer = Employer.objects.create(user=self.user,company_name='testcompany')
        self.create_cv_url= reverse('create_cv',kwargs={'user_id':self.user.id})
        self.city= Cities.objects.create(city='New York',state_name='New York')
        self.jobseeker=JobSeeker.objects.create(user=self.user,first_name='fakename',last_name='fakename',
                                                date_of_birth=date.today(),phone_number='192929',city=self.city,
                                                email='fakemail@test.me')
    def test_create_vacancy_success(self):
        self.client.force_login(self.user)
        data={
            'occupation':'engineer',
            'bio':'some info',
            'education':'bachelor',
            'schedule':'flex',
            'work_place':'flex',
            'city_id':self.city.id,
            'experience':'1',
            'salary':'12000',
            'key_skills':'None, null',
        }
        # cv=CV.objects.create()
        response = self.client.post(self.create_cv_url,data=data)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, reverse('vacancy_list',kwargs={'user_id':self.user.id}))
        self.assertEqual(CV.objects.filter(occupation='engineer').exists(),
                        True)
        
    def test_create_vacancy_failure(self):
        self.client.force_login(self.user)
        data={
                'occupation':'engineer2',
                'bio':'some info',
                'education':'bachelor',
                'schedule':'flexible',
                'work_place':'flex',
                'city_id':self.city.id,
                'experience':'1',
                'salary':'12000',
                'key_skills':'None, null',
            }
        response = self.client.post(self.create_cv_url,data=data)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, reverse('vacancy_list',kwargs={'user_id':self.user.id}))
        self.assertEqual(CV.objects.filter(occupation='engineer2').exists(),
                        False)


class EditCvTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gos.com', password='testpassword', username='testuser')
        self.city= Cities.objects.create(city='New York',state_name='New York')
        self.jobseeker=JobSeeker.objects.create(user=self.user,first_name='fakename',last_name='fakename',
                                                date_of_birth=date.today(),phone_number='192929',city=self.city,
                                                email='fakemail@test.me')
        self.cv=CV.objects.create(city=self.city,jobseeker=self.jobseeker,occupation='fakeoccupation',
                                bio='some info',education='bachelor',schedule='full',salary=10000,key_skills='some info',
                                work_place='full',experience=2)
        self.edit_cv_url= reverse('edit_cv',kwargs={'cv_id':self.user.id})
    def test_edit_cv_success(self):
        self.client.force_login(self.user)
        new_data={
            'city_id':self.city.id,
            'occupation':'new occupation',
            'bio':'another info',
            'education':'none',
            'schedule':'none',
            'salary':20000,
            'key_skills':'another info',
            'work_place':'none',
            'experience':3
        }
        response=self.client.post(self.edit_cv_url,data=new_data)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(self.cv.occupation, CV.objects.get(jobseeker=self.jobseeker).occupation)
        print(CV.objects.get(jobseeker=self.jobseeker))
        
    def test_edit_cv_failure(self):
        self.client.force_login(self.user)
        new_data={
            'city_id':self.city.id,
            'occupation':'new occupation',
            'bio':'another info',
            'education':'none',
            'schedule':'none miss',
            'salary':20000,
            'key_skills':'another info',
            'work_place':'none',
            'experience':3
        }
        response=self.client.post(self.edit_cv_url,data=new_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.cv.occupation, CV.objects.get(jobseeker=self.jobseeker).occupation)
        print(CV.objects.get(jobseeker=self.jobseeker))
        

class VacancySearchViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(email='testuser@gos.com', password='testpassword', username='testuser')
        self.city=Cities.objects.create(city='New York',state_name='New York')
        self.city2=Cities.objects.create(city='San Francisco',state_name='Florida')
        self.employer=Employer.objects.create(user=self.user,company_info='some info',company_name='testcompany',
                                            industry='industry',email='testemail@test.com',phone_number='12345',
                                            website='www.testsite.com',city=self.city)
    
    def test_cv_search(self):
        # Создание тестовых данных
        Vacancy.objects.create(city=self.city,employer=self.employer,occupation='fakeoccupation',schedule='full',
                                experience=2,education='bachelor',salary=20000,work_place='full',
                                job_description='some info',key_skills='someinfo')
        Vacancy.objects.create(city=self.city2,employer=self.employer,occupation='secondfakeoccupation',
                                schedule='full',experience=3,education='master',salary=20000,work_place='full',
                                job_description='some info',key_skills='someinfo')
        url = reverse('search_vacancy')
        data = {
            'occupation': 'fakeoccupation',
            'city_id': self.city.id,
            'experience': '1|5',
            'schedule': 'full',
            'education': 'bachelor',
            'salary': 20000,
            'work_place': 'full',
        }
        request = self.factory.get(url, data)
        response = VacancySearchView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        
        context = response.context_data
        print('CONTEXT')
        print(context)
        self.assertEqual(context['occupation'], 'fakeoccupation')
        self.assertEqual(context['city_id'], str(self.city.id))
        self.assertEqual(context['experience'], '1|5')
        self.assertEqual(context['schedule'], 'full')
        self.assertEqual(context['education'], 'bachelor')
        self.assertEqual(context['salary'], '20000')
        self.assertEqual(context['work_place'], 'full')
        
        
        # Проверка queryset
        queryset = context['vacancies']
        self.assertEqual(len(queryset), 1)
        self.assertEqual(queryset[0].occupation, 'fakeoccupation')
        self.assertEqual(queryset[0].city, self.city)
        self.assertEqual(queryset[0].experience, 2)
        self.assertEqual(queryset[0].schedule, 'full')