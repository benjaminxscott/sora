#!/usr/bin/env python

import web
import psutil
import json

# define endpoints
urls = (
    '/ps', 'process_list'
)


class process_list:
    def GET(self):
        psjson = {}
        
        for each_proc in psutil.process_iter():
            process = each_proc.as_dict(attrs=['pid', 'name', 'username','ppid','cmdline','environ']) 
            
            # Handle empty command lines 
            fmt_cmdline = False
            if process['cmdline']:
                # Convert from argv-style list of parameters to space-delimited string
                fmt_cmdline = ' '.join(process['cmdline'])
            
            # TODO convert dict of environment variables to list
            if process.get('environ') is not None:
                fmt_environs = []
                
                for each_env in process.get('environ').keys():
                    environ = each_env + '=' +  process.get('environ').get(each_env)
                    
                    fmt_environs.append( environ ) 
            else:
                fmt_environs = None
            
            # build custom dictionary
            psdict = {
                process['pid']:
                    {
                        "cmdline":fmt_cmdline,
                        "ppid":process['ppid'],
                        "name":process['name'],
                        "environment":fmt_environs
                    }
                } 
            
            
            psjson.update(psdict)
        
        return json.dumps (psjson, indent=4, sort_keys=True)

if __name__ == "__main__":
    # run our app - listening on a given port
    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 1337))
