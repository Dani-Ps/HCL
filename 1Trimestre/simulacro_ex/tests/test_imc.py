import unittest
from assignment.imc import calcular_imc

class TestIMC(unittest.TestCase):
    """
    Clase de test para probar la función calcular_imc.
    """

    def test_imc_normal(self):
        """ Prueba un caso con IMC en el rango normal. """
        self.assertAlmostEqual(calcular_imc(70, 1.75), 22.86, places=2)

    def test_imc_bajo_peso(self):
        """ Prueba un caso con IMC indicando bajo peso. """
        self.assertAlmostEqual(calcular_imc(50, 1.75), 16.33, places=2)

    def test_imc_sobrepeso(self):
        """ Prueba un caso con IMC indicando sobrepeso. """
        self.assertAlmostEqual(calcular_imc(85, 1.75), 27.76, places=2)

    def test_imc_obesidad(self):
        """ Prueba un caso con IMC indicando obesidad. """
        self.assertAlmostEqual(calcular_imc(100, 1.75), 32.65, places=2)

    def test_imc_altura_cero(self):
        """ Prueba un caso de error con altura igual a cero. """
        with self.assertRaises(ValueError):
            calcular_imc(70, 0)

    def test_imc_datos_negativos(self):
        """ Prueba casos de error con datos negativos. """
        with self.assertRaises(ValueError):
            calcular_imc(-70, 1.75)
        with self.assertRaises(ValueError):
            calcular_imc(70, -1.75)


if __name__ == '__main__':
    unittest.main()
