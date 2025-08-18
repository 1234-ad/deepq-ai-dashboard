// Dashboard JavaScript functionality

// CSRF Token for Django
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// Chart configurations
const chartColors = [
    '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
    '#FF9F40', '#FF6384', '#C9CBCF', '#4BC0C0', '#FF6384'
];

// Utility functions
function formatCurrency(value) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(value);
}

function formatNumber(value) {
    return new Intl.NumberFormat('en-US').format(value);
}

// Chart update functions
function updateChartData(chart, datasets) {
    chart.data.datasets = datasets;
    chart.update('active');
}

// Error handling
function handleApiError(error, chartName) {
    console.error(`Error fetching ${chartName} data:`, error);
    
    // Show user-friendly error message
    const errorDiv = document.createElement('div');
    errorDiv.className = 'alert alert-warning alert-dismissible fade show';
    errorDiv.innerHTML = `
        <strong>Warning:</strong> Unable to load ${chartName} data. Please try again later.
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.querySelector('.container').insertBefore(errorDiv, document.querySelector('.row'));
}

// Loading state management
function showLoading(elementId) {
    document.getElementById(elementId).classList.remove('d-none');
}

function hideLoading(elementId) {
    document.getElementById(elementId).classList.add('d-none');
}

// Data validation
function validateDateRange() {
    const startYear = parseInt(document.getElementById('startYear').value);
    const endYear = parseInt(document.getElementById('endYear').value);
    
    if (startYear > endYear) {
        alert('Start year cannot be greater than end year');
        return false;
    }
    
    if (startYear < 2000 || endYear > 2022) {
        alert('Please select years between 2000 and 2022');
        return false;
    }
    
    return true;
}

// Export functionality (bonus feature)
function exportChartData(chartData, filename) {
    const csvContent = "data:text/csv;charset=utf-8," 
        + "Country,Year,Value\n"
        + chartData.map(row => `${row.country},${row.year},${row.value}`).join("\n");
    
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", filename);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Initialize tooltips and popovers
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Add smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});