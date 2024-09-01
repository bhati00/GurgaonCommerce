import { User } from "../common/types";
import axiosInstance from "../lib/axios";

export const addUser = async (userData: Partial <User>) : Promise<User> => {
    try {
        const response = await axiosInstance.post<User>('/jwt/create', userData);
        return response.data;
      } catch (error) {
        console.error('Error updating user:', error);
        throw error;
      }
}