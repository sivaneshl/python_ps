from sharepoint import SharePointSite, basic_auth_opener

server_url = "scout.ironmountain.com"
site_url = server_url + "/functions/globalservices/IT"

opener = basic_auth_opener(server_url, 'slogandurai', 'Aug2018!')

site = SharePointSite(site_url, opener)

for sp_list in site.lists:
    print(sp_list.id, sp_list.meta['Title'])