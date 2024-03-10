export interface API {
  getVersion: () => Promise<string>
  getDownloadingStatus: () => Promise<boolean>
  readUpdateHistory: () => Promise<JSON>
}

declare global {
  interface Window {
    api: API
  }
}
