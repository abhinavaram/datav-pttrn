import React, { useState, useRef } from 'react';
import * as XLSX from 'xlsx';
import { Line } from 'react-chartjs-2';

const ExcelLineChart = () => {
  const [chartData, setChartData] = useState(null);
  const fileInputRef = useRef(null);

  const handleFileChange = () => {
    const file = fileInputRef.current.files[0];
    const reader = new FileReader();

    reader.onload = (e) => {
      const data = new Uint8Array(e.target.result);
      const workbook = XLSX.read(data, { type: 'array' });
      const sheetName = workbook.SheetNames[0]; // Assuming the first sheet is the one you want to extract data from
      const sheetData = XLSX.utils.sheet_to_json(workbook.Sheets[sheetName]);

      // Extract data dynamically based on column names
      const columnNames = Object.keys(sheetData[0]);
      const labels = sheetData.map((row) => row[columnNames[0]]);
      const datasets = columnNames
        .slice(1)
        .map((columnName, index) => ({
          label: columnName,
          data: sheetData.map((row) => row[columnName]),
          fill: false,
          borderColor: getBorderColor(index),
          tension: 0.1,
        }));

      const chartData = {
        labels,
        datasets,
      };

      setChartData(chartData);
    };

    reader.readAsArrayBuffer(file);
  };

  const getBorderColor = (index) => {
    const colors = ['rgb(75, 192, 192)', 'rgb(255, 99, 132)', 'rgb(54, 162, 235)', 'rgb(255, 205, 86)'];
    return colors[index % colors.length];
  };

  return (
    <div>
      <h1>Excel Line Chart</h1>
      <input type="file" accept=".xlsx" ref={fileInputRef} onChange={handleFileChange} />
      {chartData ? (
        <Line data={chartData} />
      ) : (
        <p>Please select an Excel file.</p>
      )}
    </div>
  );
};

export default ExcelLineChart;
