from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class FibonacciTests(APITestCase):
    def test_fibonacci_number(self):
        """
            Check results fibonacci function
        """
        lista_prueba = [0,1,2,3,6,8]
        lista_resultados = [0,1,1,2,8,21]
        
        lista_test = []
        for i in lista_prueba:
            url = reverse('fibonacci-index', args=[i] )
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            lista_test.append(response.data)    
            
        self.assertEqual(lista_test, lista_resultados)

    def test_parameters(self):
        """
            Check parameters passed in url
            Those must be positive integers
        """
        lista_prueba = [3, -1, 'aa']

        for i in lista_prueba:
            url = f'/api/fibonacci/{i}/'
            response = self.client.get(url)
            if i == 3:
                self.assertEqual(response.status_code, status.HTTP_200_OK)
            else:
                self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


        #print("URL: ", url)
        #si fuera POST
        #url = reverse('fibonacci-index')
        #data = {'index': indice}
        #response = self.client.post(url, data, format='json')
        #self.assertEqual(len(response.data), 1)
        #self.assertEqual(Account.objects.get().name, 'DabApps')
        
