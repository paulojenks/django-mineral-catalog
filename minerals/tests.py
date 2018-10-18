from django.urls import reverse
from django.test import TestCase, Client


from minerals.models import Mineral


class MineralModelTests(TestCase):
    def create_mineral(self):
        self.mineral = Mineral.objects.create(
            pk=0,
            name='Test',
            image_filename='Test',
            image_caption='Test',
            category='Test',
            formula='Test',
            strunz_classification='Test',
            crystal_system='Test',
            unit_cell='Test',
            color='Test',
            crystal_symmetry='Test',
            cleavage='Test',
            mohs_scale_hardness='Test',
            luster='Test',
            streak='Test',
            diaphaneity='Test',
            optical_properties='Test',
            refractive_index='Test',
            crystal_habit='Test',
            specific_gravity='Test',
            group='Test'
        )

    def setUp(self):
        self.client = Client()
        self.create_mineral()

    def test_mineral_creation(self):
        self.assertTrue(isinstance(self.mineral, Mineral))
        self.assertIn(self.mineral, Mineral.objects.all())

    def test_model_string(self):
        self.assertEqual(self.mineral.__str__(), self.mineral.name)

    def test_mineral_view(self):
        resp = self.client.get(reverse('minerals:index'))
        self.assertEqual(resp.status_code, 200)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_search(self):
        resp = self.client.get(reverse('minerals:search'), {'q': 'test'})
        self.assertEqual(resp.status_code, 200)

    def test_not_found(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={'pk': 9999999999}))
        self.assertEqual(resp.status_code, 404)

    def test_sort_by_letter(self):
        resp = self.client.get(reverse('minerals:letter_sort', kwargs={'letter': 'T'}))
        self.assertEqual(resp.status_code, 200)

    def test_sort_by_group(self):
        resp = self.client.get(reverse('minerals:group_sort', kwargs={'group': self.mineral.group}))
        self.assertEqual(resp.status_code, 200)

