import axios, { InternalAxiosRequestConfig } from "axios";

const axiosInstance = axios.create({
    baseURL: import.meta.env.VITE_BASE_URL, 
    headers: {
      'Content-Type': 'application/json',
    },
  });


const authExclusionRoutes = ['/'];
// Add a request interceptor
axiosInstance.interceptors.request.use(
  (config: InternalAxiosRequestConfig): InternalAxiosRequestConfig => {
    const token = localStorage.getItem('accessToken');
    if (token && !authExclusionRoutes.includes(config.url || '')) {
      // Use the `set` method to assign the Authorization header
      config.headers.set('Authorization', `Bearer ${token}`);
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
  

export default axiosInstance;