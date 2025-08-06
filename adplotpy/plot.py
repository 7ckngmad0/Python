import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import warnings
import os
from datetime import datetime
import json
from typing import Dict, List, Optional
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.offline as pyo

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class AdvancedSalesAnalyzer:
    """
    Advanced Sales Data Analysis and Visualization Class
    """
    
    def __init__(self, csv_path: str):
        """Initialize the analyzer with data path"""
        self.csv_path = csv_path
        self.df = None
        self.scaled_data = None
        self.clusters = None
        self.pca_results = None
        self.regression_model = None
        self.analysis_results = {}
        
    def load_and_preprocess_data(self) -> pd.DataFrame:
        """Load and preprocess the sales data"""
        try:
            # Use script directory for relative path
            script_dir = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(script_dir, self.csv_path)
            
            self.df = pd.read_csv(full_path)
            
            # Data quality checks
            print("=== DATA QUALITY ANALYSIS ===")
            print(f"Dataset shape: {self.df.shape}")
            print(f"Memory usage: {self.df.memory_usage(deep=True).sum() / 1024:.2f} KB")
            
            # Missing values analysis
            missing_data = self.df.isnull().sum()
            print("\nMissing values per column:")
            for col, missing in missing_data.items():
                if missing > 0:
                    print(f"  {col}: {missing} ({missing/len(self.df)*100:.2f}%)")
            
            # Data types and basic statistics
            print("\nData types:")
            print(self.df.dtypes)
            
            # Statistical summary
            print("\nStatistical Summary:")
            print(self.df.describe())
            
            return self.df
            
        except FileNotFoundError:
            print(f"Error: Could not find {self.csv_path}")
            print("Please ensure the file exists in the same directory as this script.")
            return None
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    def calculate_advanced_metrics(self) -> Dict:
        """Calculate advanced business metrics"""
        if self.df is None:
            return {}
        
        # Basic metrics
        total_sales = self.df['Sales'].sum()
        total_profit = self.df['Profit'].sum()
        
        # Advanced metrics
        self.df['Profit_Margin'] = (self.df['Profit'] / self.df['Sales']) * 100
        self.df['Sales_Rank'] = self.df['Sales'].rank(ascending=False)
        self.df['Profit_Rank'] = self.df['Profit'].rank(ascending=False)
        self.df['Efficiency_Score'] = (self.df['Profit_Margin'] * self.df['Sales']) / 1000
        
        # Statistical measures
        sales_mean = self.df['Sales'].mean()
        sales_std = self.df['Sales'].std()
        sales_cv = sales_std / sales_mean  # Coefficient of variation
        
        # Percentile analysis
        sales_percentiles = self.df['Sales'].quantile([0.25, 0.5, 0.75, 0.9, 0.95])
        
        # Performance categories
        self.df['Performance_Category'] = pd.cut(
            self.df['Sales'], 
            bins=[0, sales_percentiles[0.25], sales_percentiles[0.5], 
                  sales_percentiles[0.75], float('inf')],
            labels=['Low', 'Medium', 'High', 'Premium']
        )
        
        metrics = {
            'total_sales': total_sales,
            'total_profit': total_profit,
            'overall_profit_margin': (total_profit / total_sales) * 100,
            'sales_mean': sales_mean,
            'sales_std': sales_std,
            'sales_cv': sales_cv,
            'sales_percentiles': sales_percentiles.to_dict(),
            'top_performer': self.df.loc[self.df['Sales'].idxmax(), 'Product'],
            'most_profitable': self.df.loc[self.df['Profit'].idxmax(), 'Product']
        }
        
        self.analysis_results['metrics'] = metrics
        return metrics
    
    def perform_statistical_analysis(self) -> Dict:
        """Perform comprehensive statistical analysis"""
        if self.df is None:
            return {}
        
        # Normality tests
        sales_normality = stats.shapiro(self.df['Sales'])
        profit_normality = stats.shapiro(self.df['Profit'])
        
        # Correlation analysis
        correlation_matrix = self.df[['Sales', 'Profit', 'Profit_Margin']].corr()
        
        # Outlier detection using IQR method
        def detect_outliers(series):
            Q1 = series.quantile(0.25)
            Q3 = series.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = series[(series < lower_bound) | (series > upper_bound)]
            return outliers
        
        sales_outliers = detect_outliers(self.df['Sales'])
        profit_outliers = detect_outliers(self.df['Profit'])
        
        # Z-score analysis
        self.df['Sales_Z_Score'] = stats.zscore(self.df['Sales'])
        self.df['Profit_Z_Score'] = stats.zscore(self.df['Profit'])
        
        statistical_results = {
            'sales_normality': {
                'statistic': sales_normality.statistic,
                'p_value': sales_normality.pvalue,
                'is_normal': sales_normality.pvalue > 0.05
            },
            'profit_normality': {
                'statistic': profit_normality.statistic,
                'p_value': profit_normality.pvalue,
                'is_normal': profit_normality.pvalue > 0.05
            },
            'correlation_matrix': correlation_matrix.to_dict(),
            'sales_outliers': sales_outliers.to_dict(),
            'profit_outliers': profit_outliers.to_dict()
        }
        
        self.analysis_results['statistical'] = statistical_results
        return statistical_results
    
    def perform_clustering_analysis(self) -> Dict:
        """Perform K-means clustering analysis"""
        if self.df is None:
            return {}
        
        # Prepare data for clustering
        features = ['Sales', 'Profit', 'Profit_Margin']
        X = self.df[features].values
        
        # Standardize the data
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        self.scaled_data = X_scaled
        
        # Determine optimal number of clusters using elbow method
        inertias = []
        K_range = range(1, min(6, len(self.df) + 1))
        
        for k in K_range:
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            kmeans.fit(X_scaled)
            inertias.append(kmeans.inertia_)
        
        # Choose optimal k (simplified - in practice, you'd use elbow method)
        optimal_k = 3 if len(self.df) >= 3 else len(self.df)
        
        # Perform clustering
        kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
        self.df['Cluster'] = kmeans.fit_predict(X_scaled)
        self.clusters = kmeans
        
        # Cluster analysis
        cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
        cluster_stats = {}
        
        for i in range(optimal_k):
            cluster_data = self.df[self.df['Cluster'] == i]
            cluster_stats[f'Cluster_{i}'] = {
                'size': len(cluster_data),
                'avg_sales': cluster_data['Sales'].mean(),
                'avg_profit': cluster_data['Profit'].mean(),
                'avg_margin': cluster_data['Profit_Margin'].mean(),
                'products': cluster_data['Product'].tolist()
            }
        
        clustering_results = {
            'optimal_clusters': optimal_k,
            'inertias': inertias,
            'cluster_centers': cluster_centers.tolist(),
            'cluster_statistics': cluster_stats
        }
        
        self.analysis_results['clustering'] = clustering_results
        return clustering_results
    
    def perform_pca_analysis(self) -> Dict:
        """Perform Principal Component Analysis"""
        if self.df is None or self.scaled_data is None:
            return {}
        
        # Perform PCA
        pca = PCA()
        pca_result = pca.fit_transform(self.scaled_data)
        
        # Calculate explained variance
        explained_variance_ratio = pca.explained_variance_ratio_
        cumulative_variance = np.cumsum(explained_variance_ratio)
        
        # Get feature importance
        feature_names = ['Sales', 'Profit', 'Profit_Margin']
        pca_components = pd.DataFrame(
            pca.components_.T,
            columns=[f'PC{i+1}' for i in range(len(pca.components_))],
            index=feature_names
        )
        
        pca_results = {
            'explained_variance_ratio': explained_variance_ratio.tolist(),
            'cumulative_variance': cumulative_variance.tolist(),
            'components': pca_components.to_dict(),
            'transformed_data': pca_result.tolist()
        }
        
        self.pca_results = pca_results
        self.analysis_results['pca'] = pca_results
        return pca_results
    
    def build_regression_model(self) -> Dict:
        """Build and evaluate regression models"""
        if self.df is None:
            return {}
        
        # Prepare data
        X = self.df[['Sales']].values
        y = self.df['Profit'].values
        
        # Split data (simple split for demonstration)
        split_idx = int(len(self.df) * 0.8)
        X_train, X_test = X[:split_idx], X[split_idx:]
        y_train, y_test = y[:split_idx], y[split_idx:]
        
        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)
        
        # Calculate metrics
        train_r2 = r2_score(y_train, y_pred_train)
        test_r2 = r2_score(y_test, y_pred_test) if len(y_test) > 0 else None
        train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
        test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test)) if len(y_test) > 0 else None
        
        regression_results = {
            'coefficient': model.coef_[0],
            'intercept': model.intercept_,
            'train_r2': train_r2,
            'test_r2': test_r2,
            'train_rmse': train_rmse,
            'test_rmse': test_rmse,
            'equation': f"Profit = {model.intercept_:.2f} + {model.coef_[0]:.2f} * Sales"
        }
        
        self.regression_model = model
        self.analysis_results['regression'] = regression_results
        return regression_results
    
    def create_advanced_visualizations(self) -> None:
        """Create comprehensive visualizations using matplotlib and plotly"""
        if self.df is None:
            return
        
        # Set style
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        # Create comprehensive matplotlib visualizations with improved spacing
        fig, axes = plt.subplots(3, 3, figsize=(24, 18))
        fig.suptitle('Advanced Sales Analysis Dashboard', fontsize=18, fontweight='bold', y=0.95)
        
        # 1. Sales Distribution with KDE
        axes[0, 0].hist(self.df['Sales'], bins=10, alpha=0.7, density=True, color='skyblue', edgecolor='black')
        axes[0, 0].plot(self.df['Sales'].sort_values(), 
                        stats.gaussian_kde(self.df['Sales'])(self.df['Sales'].sort_values()), 
                        'r-', linewidth=2)
        axes[0, 0].set_title('Sales Distribution with KDE', fontsize=12, fontweight='bold')
        axes[0, 0].set_xlabel('Sales', fontsize=10)
        axes[0, 0].set_ylabel('Density', fontsize=10)
        axes[0, 0].grid(True, alpha=0.3)
        
        # 2. Profit vs Sales Scatter with regression line
        axes[0, 1].scatter(self.df['Sales'], self.df['Profit'], alpha=0.7, c='green', s=60)
        if self.regression_model:
            x_range = np.linspace(self.df['Sales'].min(), self.df['Sales'].max(), 100)
            y_pred = self.regression_model.predict(x_range.reshape(-1, 1))
            axes[0, 1].plot(x_range, y_pred, 'r-', linewidth=2, label='Regression Line')
        axes[0, 1].set_title('Profit vs Sales with Regression', fontsize=12, fontweight='bold')
        axes[0, 1].set_xlabel('Sales', fontsize=10)
        axes[0, 1].set_ylabel('Profit', fontsize=10)
        axes[0, 1].legend(loc='upper left', fontsize=9)
        axes[0, 1].grid(True, alpha=0.3)
        
        # 3. Performance Categories
        category_counts = self.df['Performance_Category'].value_counts()
        wedges, texts, autotexts = axes[0, 2].pie(category_counts.values, labels=category_counts.index, 
                                                   autopct='%1.1f%%', startangle=90)
        axes[0, 2].set_title('Performance Categories Distribution', fontsize=12, fontweight='bold')
        # Improve text visibility
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        # 4. Cluster Analysis
        if 'Cluster' in self.df.columns:
            scatter = axes[1, 0].scatter(self.df['Sales'], self.df['Profit'], 
                                        c=self.df['Cluster'], cmap='viridis', alpha=0.7, s=60)
            axes[1, 0].set_title('Clustering Results', fontsize=12, fontweight='bold')
            axes[1, 0].set_xlabel('Sales', fontsize=10)
            axes[1, 0].set_ylabel('Profit', fontsize=10)
            axes[1, 0].grid(True, alpha=0.3)
            # Position colorbar outside the plot
            cbar = plt.colorbar(scatter, ax=axes[1, 0], shrink=0.8, aspect=20)
            cbar.set_label('Cluster', fontsize=9)
        
        # 5. Z-Score Analysis
        axes[1, 1].scatter(self.df['Sales_Z_Score'], self.df['Profit_Z_Score'], alpha=0.7, s=60)
        axes[1, 1].axhline(y=0, color='r', linestyle='--', alpha=0.5)
        axes[1, 1].axvline(x=0, color='r', linestyle='--', alpha=0.5)
        axes[1, 1].set_title('Z-Score Analysis', fontsize=12, fontweight='bold')
        axes[1, 1].set_xlabel('Sales Z-Score', fontsize=10)
        axes[1, 1].set_ylabel('Profit Z-Score', fontsize=10)
        axes[1, 1].grid(True, alpha=0.3)
        
        # 6. Profit Margin Analysis - Improved bar chart
        bars = axes[1, 2].bar(range(len(self.df)), self.df['Profit_Margin'], 
                              color='orange', alpha=0.7, edgecolor='black')
        axes[1, 2].set_title('Profit Margin by Product', fontsize=12, fontweight='bold')
        axes[1, 2].set_xlabel('Product', fontsize=10)
        axes[1, 2].set_ylabel('Profit Margin (%)', fontsize=10)
        axes[1, 2].set_xticks(range(len(self.df)))
        axes[1, 2].set_xticklabels(self.df['Product'], rotation=45, ha='right')
        axes[1, 2].grid(True, alpha=0.3, axis='y')
        # Add value labels on bars
        for bar, value in zip(bars, self.df['Profit_Margin']):
            height = bar.get_height()
            axes[1, 2].text(bar.get_x() + bar.get_width()/2., height + 0.5,
                           f'{value:.1f}%', ha='center', va='bottom', fontsize=8)
        
        # 7. Efficiency Score - Improved bar chart
        bars = axes[2, 0].bar(range(len(self.df)), self.df['Efficiency_Score'], 
                              color='purple', alpha=0.7, edgecolor='black')
        axes[2, 0].set_title('Efficiency Score by Product', fontsize=12, fontweight='bold')
        axes[2, 0].set_xlabel('Product', fontsize=10)
        axes[2, 0].set_ylabel('Efficiency Score', fontsize=10)
        axes[2, 0].set_xticks(range(len(self.df)))
        axes[2, 0].set_xticklabels(self.df['Product'], rotation=45, ha='right')
        axes[2, 0].grid(True, alpha=0.3, axis='y')
        # Add value labels on bars
        for bar, value in zip(bars, self.df['Efficiency_Score']):
            height = bar.get_height()
            axes[2, 0].text(bar.get_x() + bar.get_width()/2., height + 0.5,
                           f'{value:.1f}', ha='center', va='bottom', fontsize=8)
        
        # 8. Sales Ranking - Improved bar chart
        bars = axes[2, 1].bar(range(len(self.df)), self.df['Sales_Rank'], 
                              color='teal', alpha=0.7, edgecolor='black')
        axes[2, 1].set_title('Sales Ranking', fontsize=12, fontweight='bold')
        axes[2, 1].set_xlabel('Product Index', fontsize=10)
        axes[2, 1].set_ylabel('Rank', fontsize=10)
        axes[2, 1].set_xticks(range(len(self.df)))
        axes[2, 1].set_xticklabels(self.df['Product'], rotation=45, ha='right')
        axes[2, 1].grid(True, alpha=0.3, axis='y')
        # Add value labels on bars
        for bar, value in zip(bars, self.df['Sales_Rank']):
            height = bar.get_height()
            axes[2, 1].text(bar.get_x() + bar.get_width()/2., height + 0.1,
                           f'{value:.0f}', ha='center', va='bottom', fontsize=8)
        
        # 9. Correlation Heatmap - Improved
        corr_matrix = self.df[['Sales', 'Profit', 'Profit_Margin', 'Efficiency_Score']].corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=axes[2, 2],
                   fmt='.2f', cbar_kws={'shrink': 0.8})
        axes[2, 2].set_title('Correlation Heatmap', fontsize=12, fontweight='bold')
        
        # Improve overall layout
        plt.tight_layout(pad=3.0, h_pad=2.0, w_pad=2.0)
        plt.savefig('advanced_sales_analysis.png', dpi=300, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        plt.show()
        
        # Create interactive Plotly visualizations
        self.create_interactive_plots()
    
    def create_interactive_plots(self) -> None:
        """Create interactive Plotly visualizations"""
        if self.df is None:
            return
        
        # 1. Interactive 3D Scatter Plot - Improved
        fig_3d = go.Figure(data=[go.Scatter3d(
            x=self.df['Sales'],
            y=self.df['Profit'],
            z=self.df['Profit_Margin'],
            mode='markers+text',
            marker=dict(
                size=12,
                color=self.df['Sales'],
                colorscale='Viridis',
                opacity=0.8,
                line=dict(color='black', width=1)
            ),
            text=self.df['Product'],
            textposition='middle center',
            textfont=dict(size=10, color='white'),
            hovertemplate='<b>%{text}</b><br>' +
                        'Sales: %{x}<br>' +
                        'Profit: %{y}<br>' +
                        'Profit Margin: %{z:.2f}%<br>' +
                        '<extra></extra>'
        )])
        
        fig_3d.update_layout(
            title=dict(text='3D Sales Analysis', x=0.5, font=dict(size=18)),
            scene=dict(
                xaxis_title='Sales',
                yaxis_title='Profit',
                zaxis_title='Profit Margin (%)',
                camera=dict(
                    eye=dict(x=1.5, y=1.5, z=1.5)
                ),
                aspectmode='cube'
            ),
            width=900,
            height=700,
            margin=dict(l=50, r=50, t=100, b=50),
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        
        # Save interactive plot
        fig_3d.write_html('interactive_3d_analysis.html')
        
        # 2. Interactive Dashboard - Improved layout
        fig_dashboard = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Sales by Product', 'Profit by Product', 
                          'Profit Margin by Product', 'Efficiency Score'),
            specs=[[{"type": "bar"}, {"type": "bar"}],
                   [{"type": "bar"}, {"type": "bar"}]],
            vertical_spacing=0.12,
            horizontal_spacing=0.1
        )
        
        # Add traces with improved styling
        fig_dashboard.add_trace(
            go.Bar(x=self.df['Product'], y=self.df['Sales'], name='Sales', 
                   marker_color='blue', opacity=0.8, text=self.df['Sales'], textposition='auto'),
            row=1, col=1
        )
        
        fig_dashboard.add_trace(
            go.Bar(x=self.df['Product'], y=self.df['Profit'], name='Profit', 
                   marker_color='green', opacity=0.8, text=self.df['Profit'], textposition='auto'),
            row=1, col=2
        )
        
        fig_dashboard.add_trace(
            go.Bar(x=self.df['Product'], y=self.df['Profit_Margin'], name='Profit Margin', 
                   marker_color='orange', opacity=0.8, text=[f'{x:.1f}%' for x in self.df['Profit_Margin']], 
                   textposition='auto'),
            row=2, col=1
        )
        
        fig_dashboard.add_trace(
            go.Bar(x=self.df['Product'], y=self.df['Efficiency_Score'], name='Efficiency Score', 
                   marker_color='purple', opacity=0.8, text=[f'{x:.1f}' for x in self.df['Efficiency_Score']], 
                   textposition='auto'),
            row=2, col=2
        )
        
        # Update layout with better spacing and styling
        fig_dashboard.update_layout(
            title=dict(text='Interactive Sales Dashboard', x=0.5, font=dict(size=20)),
            height=900,
            width=1200,
            showlegend=False,
            margin=dict(l=50, r=50, t=100, b=50),
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        
        # Update axes for better readability
        fig_dashboard.update_xaxes(tickangle=45, tickfont=dict(size=10))
        fig_dashboard.update_yaxes(tickfont=dict(size=10))
        
        # Add grid lines
        for i in range(1, 3):
            for j in range(1, 3):
                fig_dashboard.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', row=i, col=j)
                fig_dashboard.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', row=i, col=j)
        
        # Save dashboard
        fig_dashboard.write_html('interactive_dashboard.html')
        
        print("Interactive visualizations saved as 'interactive_3d_analysis.html' and 'interactive_dashboard.html'")
    
    def create_individual_plots(self) -> None:
        """Create individual high-quality plots for better control over layout"""
        if self.df is None:
            return
        
        # Set style
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        # 1. Sales Distribution
        plt.figure(figsize=(12, 8))
        plt.hist(self.df['Sales'], bins=10, alpha=0.7, density=True, color='skyblue', edgecolor='black')
        plt.plot(self.df['Sales'].sort_values(), 
                stats.gaussian_kde(self.df['Sales'])(self.df['Sales'].sort_values()), 
                'r-', linewidth=2)
        plt.title('Sales Distribution with KDE', fontsize=16, fontweight='bold')
        plt.xlabel('Sales', fontsize=12)
        plt.ylabel('Density', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('sales_distribution.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # 2. Profit vs Sales Scatter
        plt.figure(figsize=(12, 8))
        plt.scatter(self.df['Sales'], self.df['Profit'], alpha=0.7, c='green', s=100)
        if self.regression_model:
            x_range = np.linspace(self.df['Sales'].min(), self.df['Sales'].max(), 100)
            y_pred = self.regression_model.predict(x_range.reshape(-1, 1))
            plt.plot(x_range, y_pred, 'r-', linewidth=2, label='Regression Line')
        plt.title('Profit vs Sales with Regression', fontsize=16, fontweight='bold')
        plt.xlabel('Sales', fontsize=12)
        plt.ylabel('Profit', fontsize=12)
        plt.legend(fontsize=10)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('profit_vs_sales.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # 3. Bar Charts with better spacing
        fig, axes = plt.subplots(2, 2, figsize=(20, 12))
        
        # Sales by Product
        bars = axes[0, 0].bar(range(len(self.df)), self.df['Sales'], 
                              color='blue', alpha=0.7, edgecolor='black')
        axes[0, 0].set_title('Sales by Product', fontsize=14, fontweight='bold')
        axes[0, 0].set_xlabel('Product', fontsize=12)
        axes[0, 0].set_ylabel('Sales', fontsize=12)
        axes[0, 0].set_xticks(range(len(self.df)))
        axes[0, 0].set_xticklabels(self.df['Product'], rotation=45, ha='right')
        axes[0, 0].grid(True, alpha=0.3, axis='y')
        for bar, value in zip(bars, self.df['Sales']):
            height = bar.get_height()
            axes[0, 0].text(bar.get_x() + bar.get_width()/2., height + 10,
                           f'{value:.0f}', ha='center', va='bottom', fontsize=10)
        
        # Profit by Product
        bars = axes[0, 1].bar(range(len(self.df)), self.df['Profit'], 
                              color='green', alpha=0.7, edgecolor='black')
        axes[0, 1].set_title('Profit by Product', fontsize=14, fontweight='bold')
        axes[0, 1].set_xlabel('Product', fontsize=12)
        axes[0, 1].set_ylabel('Profit', fontsize=12)
        axes[0, 1].set_xticks(range(len(self.df)))
        axes[0, 1].set_xticklabels(self.df['Product'], rotation=45, ha='right')
        axes[0, 1].grid(True, alpha=0.3, axis='y')
        for bar, value in zip(bars, self.df['Profit']):
            height = bar.get_height()
            axes[0, 1].text(bar.get_x() + bar.get_width()/2., height + 5,
                           f'{value:.0f}', ha='center', va='bottom', fontsize=10)
        
        # Profit Margin by Product
        bars = axes[1, 0].bar(range(len(self.df)), self.df['Profit_Margin'], 
                              color='orange', alpha=0.7, edgecolor='black')
        axes[1, 0].set_title('Profit Margin by Product', fontsize=14, fontweight='bold')
        axes[1, 0].set_xlabel('Product', fontsize=12)
        axes[1, 0].set_ylabel('Profit Margin (%)', fontsize=12)
        axes[1, 0].set_xticks(range(len(self.df)))
        axes[1, 0].set_xticklabels(self.df['Product'], rotation=45, ha='right')
        axes[1, 0].grid(True, alpha=0.3, axis='y')
        for bar, value in zip(bars, self.df['Profit_Margin']):
            height = bar.get_height()
            axes[1, 0].text(bar.get_x() + bar.get_width()/2., height + 0.5,
                           f'{value:.1f}%', ha='center', va='bottom', fontsize=10)
        
        # Efficiency Score by Product
        bars = axes[1, 1].bar(range(len(self.df)), self.df['Efficiency_Score'], 
                              color='purple', alpha=0.7, edgecolor='black')
        axes[1, 1].set_title('Efficiency Score by Product', fontsize=14, fontweight='bold')
        axes[1, 1].set_xlabel('Product', fontsize=12)
        axes[1, 1].set_ylabel('Efficiency Score', fontsize=12)
        axes[1, 1].set_xticks(range(len(self.df)))
        axes[1, 1].set_xticklabels(self.df['Product'], rotation=45, ha='right')
        axes[1, 1].grid(True, alpha=0.3, axis='y')
        for bar, value in zip(bars, self.df['Efficiency_Score']):
            height = bar.get_height()
            axes[1, 1].text(bar.get_x() + bar.get_width()/2., height + 0.5,
                           f'{value:.1f}', ha='center', va='bottom', fontsize=10)
        
        plt.tight_layout(pad=3.0)
        plt.savefig('product_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("Individual plots saved as 'sales_distribution.png', 'profit_vs_sales.png', and 'product_analysis.png'")
    
    def generate_comprehensive_report(self) -> None:
        """Generate a comprehensive analysis report"""
        if not self.analysis_results:
            return
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'data_summary': {
                'total_products': len(self.df),
                'total_sales': self.analysis_results['metrics']['total_sales'],
                'total_profit': self.analysis_results['metrics']['total_profit'],
                'overall_profit_margin': self.analysis_results['metrics']['overall_profit_margin']
            },
            'key_findings': {
                'top_performer': self.analysis_results['metrics']['top_performer'],
                'most_profitable': self.analysis_results['metrics']['most_profitable'],
                'sales_volatility': self.analysis_results['metrics']['sales_cv'],
                'data_normality': {
                    'sales_normal': self.analysis_results['statistical']['sales_normality']['is_normal'],
                    'profit_normal': self.analysis_results['statistical']['profit_normality']['is_normal']
                }
            },
            'clustering_insights': self.analysis_results.get('clustering', {}),
            'regression_insights': self.analysis_results.get('regression', {}),
            'recommendations': self.generate_recommendations()
        }
        
        # Save report as JSON
        with open('comprehensive_analysis_report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        # Print summary
        print("\n" + "="*60)
        print("COMPREHENSIVE ANALYSIS REPORT")
        print("="*60)
        print(f"Analysis completed at: {report['timestamp']}")
        print(f"Total Products Analyzed: {report['data_summary']['total_products']}")
        print(f"Total Sales: ${report['data_summary']['total_sales']:,.2f}")
        print(f"Total Profit: ${report['data_summary']['total_profit']:,.2f}")
        print(f"Overall Profit Margin: {report['data_summary']['overall_profit_margin']:.2f}%")
        print(f"Top Performer: {report['key_findings']['top_performer']}")
        print(f"Most Profitable: {report['key_findings']['most_profitable']}")
        print(f"Sales Volatility (CV): {report['key_findings']['sales_volatility']:.2f}")
        
        if 'regression_insights' in report and report['regression_insights']:
            print(f"Regression R² Score: {report['regression_insights']['train_r2']:.3f}")
            print(f"Regression Equation: {report['regression_insights']['equation']}")
        
        print("\nRecommendations:")
        for rec in report['recommendations']:
            print(f"• {rec}")
        
        print("\nReport saved as 'comprehensive_analysis_report.json'")
        print("="*60)
    
    def generate_recommendations(self) -> List[str]:
        """Generate business recommendations based on analysis"""
        recommendations = []
        
        if not self.analysis_results:
            return recommendations
        
        metrics = self.analysis_results['metrics']
        
        # Sales-based recommendations
        if metrics['sales_cv'] > 0.5:
            recommendations.append("High sales volatility detected - consider diversifying product portfolio")
        
        # Profit margin recommendations
        if metrics['overall_profit_margin'] < 40:
            recommendations.append("Overall profit margin is below optimal - review pricing strategy")
        
        # Top performer analysis
        top_product = metrics['top_performer']
        top_product_data = self.df[self.df['Product'] == top_product].iloc[0]
        if top_product_data['Profit_Margin'] < 50:
            recommendations.append(f"Top seller '{top_product}' has low profit margin - consider price optimization")
        
        # Clustering insights
        if 'clustering' in self.analysis_results:
            cluster_stats = self.analysis_results['clustering']['cluster_statistics']
            for cluster_name, stats in cluster_stats.items():
                if stats['avg_margin'] < 40:
                    recommendations.append(f"Cluster {cluster_name} shows low profitability - needs attention")
        
        # Regression insights
        if 'regression' in self.analysis_results:
            reg_results = self.analysis_results['regression']
            if reg_results['train_r2'] < 0.7:
                recommendations.append("Weak correlation between sales and profit - investigate pricing strategy")
        
        return recommendations
    
    def run_complete_analysis(self) -> None:
        """Run the complete analysis pipeline"""
        print("Starting Advanced Sales Analysis...")
        print("="*50)
        
        # Load and preprocess data
        self.load_and_preprocess_data()
        if self.df is None:
            return
        
        # Perform all analyses
        print("\nCalculating advanced metrics...")
        self.calculate_advanced_metrics()
        
        print("\nPerforming statistical analysis...")
        self.perform_statistical_analysis()
        
        print("\nPerforming clustering analysis...")
        self.perform_clustering_analysis()
        
        print("\nPerforming PCA analysis...")
        self.perform_pca_analysis()
        
        print("\nBuilding regression model...")
        self.build_regression_model()
        
        print("\nCreating visualizations...")
        self.create_advanced_visualizations()
        
        print("\nCreating individual plots...")
        self.create_individual_plots()
        
        print("\nGenerating comprehensive report...")
        self.generate_comprehensive_report()
        
        # Save enhanced dataset
        self.df.to_csv('enhanced_sales_data.csv', index=False)
        print("\nEnhanced dataset saved as 'enhanced_sales_data.csv'")
        
        print("\nAnalysis complete! Check the generated files for detailed results.")

def main():
    """Main execution function"""
    analyzer = AdvancedSalesAnalyzer('sales_data.csv')
    analyzer.run_complete_analysis()

if __name__ == "__main__":
    main()