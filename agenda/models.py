# -*- encoding: utf-8 -*-
from datetime import datetime
from django.db import models


class UF(models.Model):
	'''
	Uma Unidade Federativa
	'''
	nome = models.CharField(max_length=100)
	sigla = models.CharField(max_length=3)

	def __unicode__(self):
		return self.nome

	class Meta:
		verbose_name = 'estado'
		ordering = ('nome',)


class Municipio(models.Model):
	'''
	Município de uma UF
	'''
	nome = models.CharField(max_length=100)
	uf = models.ForeignKey(UF, verbose_name='UF')
	codigo = models.IntegerField(
	blank=True, null=True, verbose_name='código')

	def __unicode__(self):
		return "%s, %s" % (self.nome, self.uf.sigla)

	class Meta:
		verbose_name = 'município'


class Bairro(models.Model):
	'''
	Bairro de um município
	'''
	nome = models.CharField(max_length=100, verbose_name='nome')
	municipio = models.ForeignKey(Municipio, related_name='bairros',
	verbose_name=u'município',
	on_delete=models.PROTECT)
	codigo = models.IntegerField(blank=True, null=True,
	verbose_name=u'código')

	def __unicode__(self):
		return "%s" % (self.nome,)

	class Meta:
		ordering = ('municipio', 'nome',)

class Usuario(models.Model):
	class meta:
		ordering = ('nome','sobrenome',)

	nome = models.CharField(max_length=100)
	sobrenome = models.CharField(max_length=100)
	nome_completo = models.CharField(max_length=255)
	email = models.EmailField(blank=True, verbose_name='e-mail')
	cpf = models.BigIntegerField(verbose_name='CPF', unique=True)
	cadastro = models.DateTimeField(default=datetime.now, blank=True)

	def __unicode__(self):
		return self.get_nome_completo()

	def get_nome_completo(self):
		return '%s %s' % (self.nome, self.sobrenome)

	class Meta:
		verbose_name = u'usuário'
		verbose_name_plural = u'usuários'
		ordering = ('nome','sobrenome',)

class ItemAgenda(models.Model):
	data = models.DateField(verbose_name='Data',)
	hora = models.TimeField(verbose_name='Hora',)
	titulo = models.CharField(verbose_name=u'Título',max_length=100,)
	descricao = models.TextField(verbose_name=u'Descrição',)
	usuario = models.ForeignKey(Usuario)
	participantes = models.ManyToManyField(Usuario, related_name="item_participantes")

	def __unicode__(self):
		return u"%s - %s %s" % (self.titulo, self.data, self.hora)	

	class Meta:
		verbose_name = u'Item Agenda'
		verbose_name_plural = u'Itens Agenda'