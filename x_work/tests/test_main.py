from django.test import TestCase, RequestFactory, Client
from main.models import User, Cities, Occupation
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import JsonResponse
from main.services import UserService
from main.views import get_city,get_occupation
from employers.models import Employer
from job_seekers.models import JobSeeker
import json
import datetime
import tempfile
from django.core.files import File
from django.core.files.images import ImageFile

from django.core.files.uploadedfile import SimpleUploadedFile



class LoginTestCase(TestCase):
    def setUp(self):
        
        self.login_url = reverse('login')
        self.user = User.objects.create_user(email='testuser@gos.com', password='testpassword', username='testuser')

    def test_login_success(self):
        response = self.client.post(self.login_url, {'username': 'testuser@gos.com', 'password': 'testpassword'},)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertRedirects(response, reverse('main_page'))

    def test_login_failure(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertTemplateUsed(response, 'login.html')

class RegistrationTestCase(TestCase):
    def setUp(self):
        self.register_url = reverse('register')  # Проверьте, что 'register' - это правильное имя вашего URL-шаблона

    def test_registration_jobseeker_success(self):
        # Создаем данные для отправки формы регистрации
        form_data = {
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'user_type':'jobseeker',
            'first_name':'pavel',
            'last_name':'dankin',
            'phone_number':'12012031023',
            # 'city_id':1
        }
        city_id=Cities.objects.create(city='New York', state_name='New York').id
        form_data['city_id']=city_id
        response = self.client.post(self.register_url, form_data)

        self.assertEqual(response.status_code, 200)
        
        self.assertTrue(User.objects.filter(email=form_data['email']).exists())

    def test_registration_jobseeker_failure(self):
        
        form_data = {
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'differentpassword',
            'user_type':'jobseeker',
            'first_name':'pavel',
            'last_name':'dankin',
            'phone_number':'12012031023',
            
            
        }
        city_id=Cities.objects.create(city='New York', state_name='New York').id
        form_data['city_id']=city_id
        response = self.client.post(self.register_url, form_data)

        self.assertEqual(response.status_code, 200)

        
        self.assertFalse(User.objects.filter(email=form_data['email']).exists())

    def test_registration_company_success(self):
        # Создаем данные для отправки формы регистрации
        form_data = {
            'email': 'testcompany@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'user_type':'company',
            'company_name':'company',
            'phone_number':'12012031023',
            
        }
        city_id=Cities.objects.create(city='New York', state_name='New York').id
        form_data['city_id']=city_id
        response = self.client.post(self.register_url, form_data)

        self.assertEqual(response.status_code, 200)
        
        self.assertTrue(User.objects.filter(email=form_data['email']).exists())
    
    def test_registration_company_failure(self):
        # Создаем данные для отправки формы регистрации
        form_data = {
            'email': 'testcompany@example.com',
            'password1': 'testpassword',
            'password2': 'testpasswordc',
            'user_type':'company',
            'company_name':'company',
            'phone_number':'12012031023',
            
        }
        city_id=Cities.objects.create(city='New York', state_name='New York').id
        form_data['city_id']=city_id
        response = self.client.post(self.register_url, form_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(email=form_data['email']).exists())



class GetCityTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_city(self):
        # Создаем GET-запрос с параметром 'search'
        Cities.objects.create(city='New York', state_name='New York')
        Cities.objects.create(city='New Orleans', state_name='Louisiana')
        Cities.objects.create(city='New Haven', state_name='Connecticut')
        Cities.objects.create(city='Las Vegas', state_name='Texas')
        Cities.objects.create(city='Alaska', state_name='Alaska')
        request = self.factory.get('/get_city', {'search': 'New'})
        # print('request')
        # print(request)
        # print('request')
        response = get_city(request)
        
        self.assertEqual(response.status_code, 200)
        
        content = response.content.decode('utf-8')
        response=json.loads(content)

        expected_payload = {
            'status': True,
            'payload': [
                {'city': 'New York', 'state': 'New York', 'id': 1},
                {"city": "New Orleans", "state": "Louisiana", "id": 2},
                {"city": "New Haven", "state": "Connecticut", "id": 3}
            ]
        }
        self.assertEqual(response, expected_payload)
        
        request = self.factory.get('/get_city', {'search': 'Ala'})
        response = get_city(request)
        
        self.assertEqual(response.status_code, 200)
        
        content = response.content.decode('utf-8')
        response=json.loads(content)

        expected_payload = {
            'status': True,
            'payload': [
                {'city': 'Alaska', 'state': 'Alaska', 'id': 5},
            ]
        }
        self.assertEqual(response, expected_payload)


class GetCityTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    def test_get_occupation(self):
        Occupation.objects.create(occupation='Dantist')
        Occupation.objects.create(occupation='Nurse')
        Occupation.objects.create(occupation='Teacher')
        Occupation.objects.create(occupation='Policeman')
        Occupation.objects.create(occupation='Programmer')
        Occupation.objects.create(occupation='Actor')
        request = self.factory.get('/get_occupation', {'search': 'P'})
        
        response = get_occupation(request)
        
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        response=json.loads(content)

        expected_payload = {
            'status': True,
            'payload': [
                {'occupation': 'Policeman', 'id': 4},
                {'occupation': 'Programmer', 'id': 5},
            ]
        }
        self.assertEqual(response, expected_payload)

        request = self.factory.get('/get_occupation', {'search': 'Nu'})
        
        response = get_occupation(request)
        
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        response=json.loads(content)

        expected_payload = {
            'status': True,
            'payload': [
                {'occupation': 'Nurse', 'id': 2},
                
            ]
        }
        self.assertEqual(response, expected_payload)

class EditProfileMainInfoTestCase(TestCase):
    # with open('tests/testphoto.jpg', 'rb') as file:
    #         uploaded_image_global = SimpleUploadedFile(file.name, file.read(), content_type='image/jpeg')
    
    def setUp(self):
        # self.login_url = reverse('login')
        
        self.user = User.objects.create_user(email='testcompany@gos.com', password='testpassword', username='testuser',user_type='company')
        self.user_jobseeker = User.objects.create_user(email='testjobseeker@gos.com', password='testpassword', username='testuser',user_type='jobseeker')
        
    def test_01_edit_main_profile_company_success(self):
        city=Cities.objects.create(city='City',state_name='State')
        employer=Employer.objects.create(user=self.user,company_name='testcompany',company_info='some info',
                                industry='industry',email=self.user.email, phone_number='129292',
                                website='www.testsite.com',city=city)
        self.assertTrue(Employer.objects.filter(user=self.user).exists())
        first_values=Employer.objects.get(user=self.user).__dict__
        image_path = 'tests/testphoto.jpg'
        with open(image_path, 'rb') as file:
        
            uploaded_image = SimpleUploadedFile(file.name, file.read(), content_type='image/jpeg')

        
        new_data={'company_name':'test', 'website':'www.newwebsite.com','profile_photo':uploaded_image,
                    'phone_number':'18888','industry':'newindustry','company_info':'some','city_id':city.id,'user':self.user}
        self.client.force_login(self.user)                    
        self.client.post(reverse('edit_profile'),new_data,format='multipart')
        second_values=Employer.objects.get(user=self.user).__dict__
        self.assertNotEqual(first_values, second_values)
    def test_02_edit_main_profile_jobseeker_success(self):
        
        city=Cities.objects.create(city='City',state_name='State')
        jobseeker= JobSeeker.objects.create(user=self.user_jobseeker,first_name='first_name_test',
                                            last_name='last_name_test',date_of_birth=datetime.date.today(),
                                            phone_number='12345678',city=city,email=self.user_jobseeker.email)
        self.assertTrue(JobSeeker.objects.filter(user=self.user_jobseeker).exists())
        first_values=JobSeeker.objects.get(user=self.user_jobseeker).__dict__
        image_path = 'tests/testphoto.jpg'
        with open(image_path, 'rb') as file:
        
            uploaded_image = SimpleUploadedFile(file.name, file.read(), content_type='image/jpeg')

        new_data={'first_name':'second first name', 'last_name':'second last name',
                    'profile_photo':uploaded_image,'phone_number':'18888','city_id':city.id,'user':self.user_jobseeker}
        self.client.force_login(self.user_jobseeker)                    
        self.client.post(reverse('edit_profile'),new_data,format='multipart')
        second_values=JobSeeker.objects.get(user=self.user_jobseeker).__dict__
        self.assertNotEqual(first_values, second_values)


    
    # def test_edit_main_profile_info_failure(self):
    #     Cities.objects.create(city='Citys', state_name='Statesss')
        
    #     city=Cities.objects.create(city='City2',state_name='State')

    #     employer=Employer.objects.create(user=self.user,company_name='testcompany',company_info='some info',
    #                             industry='industry',email=self.user.email, phone_number='129292',
    #                             website='www.testsite.com',city=city)
    #     self.assertTrue(Employer.objects.filter(user=self.user).exists())
        
    #     first_values=Employer.objects.get(user=self.user).__dict__
    #     image_path = 'tests/testphoto.jpg'
    #     print('user2:')
    #     print(Employer.objects.get(user=self.user).__dict__.items())
    #     with open(image_path, 'rb') as file:
        
    #         uploaded_image_two = file.read()
         
    #     new_data={'company_name':'test', 'website':'newwebsit','profile_photo':uploaded_image_two,
    #                 'phone_number':'18888','industry':'newindustry','company_info':'some','city_id':city.id,'user':self.user}
    #     self.client.force_login(self.user)                    
    #     self.client.post(reverse('edit_profile'),new_data,format='multipart')
    #     second_values=Employer.objects.get(user=self.user).__dict__
    #     print('user2:')
    #     print(Employer.objects.get(user=self.user).__dict__.items())
        # self.assertEqual(first_values, second_values)
        
        
        # self.assertEqual(first_values, last_values)

