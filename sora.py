#!/usr/bin/env python

import web
import psutil
import json

# define our endpoints
urls = (
    '/ps', 'process_list'
)


class process_list:
    def GET(self):
        psjson = {}
        
        # Get a list of all non-root processes on the local system
        for each_proc in psutil.process_iter():
            
            # Pull out process metadata that we want to return
            process = each_proc.as_dict(attrs=['pid', 'name', 'username','ppid','cmdline','environ']) 
            
            # Handle empty command lines - treated as 'false' if empty
            fmt_cmdline = False
            if process['cmdline']:
                # Convert our command line from argv-style list of parameters to space-delimited string
                fmt_cmdline = ' '.join(process['cmdline'])
                
            # skip the agent process - don't show it in process results 
            if "sora.py" in fmt_cmdline:
                continue
            
            # convert dict of environment variables to a list
            if process.get('environ') is not None:
                fmt_environs = []
                
                for each_env in process.get('environ').keys():
                    environ = each_env + '=' +  process.get('environ').get(each_env)
                    
                    fmt_environs.append( environ ) 
            else:
                fmt_environs = None
            
            # build dict to be returned as json
            psdict = {
                process['pid']:
                    {
                        "cmdline":fmt_cmdline,
                        "ppid":process['ppid'],
                        "name":process['name'],
                        "environment":fmt_environs
                    }
                } 
            
            # add our dict to the overall
            psjson.update(psdict)
        
        # endfunc
        return json.dumps (psjson, indent=4, sort_keys=True)

if __name__ == "__main__":
    # run our app - listening on a given port
    app = web.application(urls, globals())
    # note that SSL is not currently supported
    web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 1337))
