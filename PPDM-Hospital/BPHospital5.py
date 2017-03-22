import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pylab

class BPHospital5:
	def __init__(self):
		self.frequencyfinal=list()
		self.details=["Very Low", "Low", "Moderately Low", "Moderate", "Higher Moderate", "High", "Very High", "Risky"]
	
	def EncryptBPCategory(self,e):
		workbook = xlrd.open_workbook('data\data5.xls')

		worksheet = workbook.sheet_by_index(0)
		max_rows= worksheet.nrows
		max_columns= worksheet.ncols

		parameters=list()
		finalparameters=list()
		data=list()
		isfloat=list()

		validcolumn=[9,10,12,13,14,15,16,17]

		def ispresent(k,a):
			for i in range(len(a)):
				if a[i]==k:
					return True
			return False
			

		for i in range(max_columns):
				isfloat.append("false");
				parameters.append(str(worksheet.cell(0,i).value))

				
		for i in range(1,max_rows):
			for j in range(max_columns):
				if isinstance(worksheet.cell(i,j).value,(int, long, float)):
					isfloat[j]="true"		
				
		for i in range(1,max_rows):
			tempdata=list()
			for j in range(max_columns):
				if isfloat[j]=="true" and ispresent(j,validcolumn):
					if worksheet.cell(i,j).value=="":
						tempdata.append(0.00)
					else:	
						tempdata.append(float(worksheet.cell(i,j).value))
			data.append(tempdata)

		for i in range(max_columns):
			if isfloat[i]=="true" and ispresent(i,validcolumn):
				line=str(worksheet.cell(0,i).value)
				for char in line:
					if char in " ?.!/;:":
						line=line.replace(char,'')
				finalparameters.append(line)


		x=pd.DataFrame(data)
		x.columns=finalparameters
		#print x


		model=KMeans(n_clusters=8)
		model.fit(x)

		print model.labels_
		temp=list(model.cluster_centers_)
		temp1=list()
		temp2=list()
		for i in range(len(temp)):
			temp1.append(sum(temp[i]))
			temp2.append(sum(temp[i]))

		temp2.sort()

		print temp1
		print temp2
		categoryorder=list()
		for i in range(len(temp)):
			for j in range(len(temp)):
				if temp2[i]==temp1[j]:
					categoryorder.append(j)



				
		"""
		colormap=np.array(["Red","Blue","Green","Yellow","Violet","Pink","Orange","Black"])


		fig = plt.figure()
		fig.suptitle('Blood Pressure Plot', fontsize=20)
		plt.scatter(x.height,x.weight,c=colormap[model.labels_])
		plt.xlabel('Height')
		plt.ylabel('Weight')
		pylab.show()


		fig = plt.figure()
		fig.suptitle('Blood Pressure Plot', fontsize=20)
		plt.scatter(x.bp1s,x.bp1d,c=colormap[model.labels_])
		plt.xlabel('Bp1s')
		plt.ylabel('Bp1d')
		pylab.show()

		fig = plt.figure()
		fig.suptitle('Blood Pressure Plot', fontsize=20)
		plt.scatter(x.bp2s,x.bp2d,c=colormap[model.labels_])
		plt.xlabel('Bp2s')
		plt.ylabel('Bp2d')
		pylab.show()


		fig = plt.figure()
		fig.suptitle('Blood Pressure Plot', fontsize=20)
		plt.scatter(x.waist,x.hip,c=colormap[model.labels_])
		plt.xlabel('Waist')
		plt.ylabel('Hip')
		pylab.show()
		"""
		frequency=list()
		category=list(model.labels_)
		#print type(model.labels_)
		for i in range(8):
			frequency.append(category.count(i))
			self.frequencyfinal.append(0)

			
		for i in range(len(categoryorder)):			
			self.frequencyfinal[i]=frequency[categoryorder[i]]

		fig = plt.figure()

		width = .35
		ind = np.arange(len(self.frequencyfinal))
		plt.bar(ind, self.frequencyfinal, width=width)
		plt.xticks(ind + width / 2, self.details)

		fig.autofmt_xdate()

		plt.savefig("figure_bp5.pdf")
		e=self.EncryptedSum(e)
		return e
		
	
	def PlotwithMean(self,d):
		n_groups = 8
		details1=['VL','L','ML','M','HM','H','VH','R']
		means = (10,10,10,10,10,10,10,10)
		# create plot
		fig, ax = plt.subplots()
		index = np.arange(n_groups)
		bar_width = 0.35
		opacity = 0.8
		 
		rects1 = plt.bar(index, self.frequencyfinal, bar_width,
						 alpha=opacity,
						 color='b',
						 label='Individual Data')
		 
		rects2 = plt.bar(index + bar_width, means, bar_width,
						 alpha=opacity,
						 color='g',
						 label='Meaned Data Across Hospitals')
		 
		plt.xlabel('Severity of Disease')
		plt.ylabel('Frequency of People')
		plt.title('Frequency of person under a severity of disease')
		plt.xticks(index + bar_width, details1)
		plt.legend()
		 
		plt.tight_layout()

		plt.savefig("compare5.pdf")
		
	def EncryptedSum(self,e):
		""" We need to write a function which will add the encrypted parameter e with encrypted value of  self.frequencyfinal
			It should return resultant encrypted value
			f=es_add(e+encrypt(self.frequencyfinal))
			return f
		"""