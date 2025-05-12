import unittest
from unittest.mock import patch, MagicMock
from auth import obter_token
from query import buscar_baterias
from requests import RequestException


class TestAuth(unittest.TestCase):
    @patch("auth.requests.post")
    def test_obter_token_sucesso(self, mock_post):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"token": "abc123"}
        mock_post.return_value = mock_response

        print("json simulado: ", mock_response.json())

        token = obter_token()
        self.assertEqual(token, "abc123")

    @patch("auth.requests.post")
    def test_obter_token_erro(self, mock_post):
        mock_post.side_effect = RequestException("Falha na requisição")
        token = obter_token()
        self.assertIsNone(token)

class TestQuery(unittest.TestCase):
    @patch("query.requests.post")
    def test_buscar_baterias_sucesso(self, mock_post):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = [
            {"email": "teste@email.com", "data_agendamento": "01/01/2100", "horario_agendamento": "15h", "qtde_pessoas": "5"}
        ]
        mock_post.return_value = mock_response

        print("json simulado: ", mock_response.json())


        dados = buscar_baterias("token123", "teste@email.com")
        self.assertEqual(len(dados), 1)
        self.assertEqual(dados[0]["email"], "teste@email.com")

    @patch("query.requests.post")
    def test_buscar_baterias_falha(self, mock_post):
        mock_post.side_effect = RequestException("Erro")
        dados = buscar_baterias("token123", "email@exemplo.com")
        self.assertEqual(dados, [])

if __name__ == "__main__":
    unittest.main()
